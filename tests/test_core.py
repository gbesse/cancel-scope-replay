import unittest
from cancel_scope_replay import run
class Tests(unittest.TestCase):
 def test_structured_scope_cancels_child_before_gate(self):
  r=run({'modes':['taskgroup']})['runs'][0];self.assertEqual(r['effects_before_gate_release'],['cancelled']);self.assertFalse(r['effect_survived_parent_cancel']);self.assertTrue(r['all_children_finished'])
 def test_detached_and_shielded_tasks_outlive_parent(self):
  for mode in ['detached','shield']:
   r=run({'modes':[mode]})['runs'][0];self.assertEqual(r['effects_before_gate_release'],[]);self.assertEqual(r['effects_after_gate_release'],['effect']);self.assertTrue(r['all_children_finished'])
 def test_repeated_runs_are_deterministic_without_sleep_races(self):
  self.assertEqual(run({}),run({}))
 def test_unknown_mode_rejected(self):
  with self.assertRaises(ValueError):run({'modes':['unknown']})
