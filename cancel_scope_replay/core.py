import asyncio

async def replay(mode):
 started=asyncio.Event();release=asyncio.Event();effects=[];children=[]
 async def child():
  started.set()
  try:await release.wait();effects.append('effect')
  except asyncio.CancelledError:effects.append('cancelled');raise
 async def parent():
  if mode=='taskgroup':
   async with asyncio.TaskGroup()as group:
    children.append(group.create_task(child()));await asyncio.Future()
  elif mode=='detached':
   children.append(asyncio.create_task(child()));await asyncio.Future()
  elif mode=='shield':
   children.append(asyncio.create_task(child()));await asyncio.shield(children[0])
  else:raise ValueError('mode')
 p=asyncio.create_task(parent());await started.wait();p.cancel()
 try:await p
 except asyncio.CancelledError:pass
 after_cancel=list(effects);release.set()
 for task in children:
  try:await task
  except asyncio.CancelledError:pass
 return {'mode':mode,'effects_before_gate_release':after_cancel,'effects_after_gate_release':effects,'effect_survived_parent_cancel':'effect'in effects,'all_children_finished':all(t.done()for t in children)}
def run(data):
 modes=data.get('modes',['taskgroup','detached','shield'])
 if not isinstance(modes,list)or not modes or len(modes)>10 or any(m not in ('taskgroup','detached','shield')for m in modes):raise ValueError('modes')
 return {'runs':[asyncio.run(replay(mode))for mode in modes],'model':'actual_asyncio_event_gated_tasks_no_external_side_effects'}
