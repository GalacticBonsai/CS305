from pyDatalog import pyDatalog
from a7 import load_course_catalog, load_graduation_rules, assert_student_completed_class, ask_if_graduated, find_graduates
import math
import types   
from operator import lt,ne,eq,gt
    
# Unit tests for CS305 Unit 7 homework assignment 

def test_1():
  """loading catalog"""
  pyDatalog.clear()
  load_course_catalog()
  assert pyDatalog.ask("subject('cs101','stem')"), "cs101 not loaded"
  assert pyDatalog.ask("subject('mat167','stem')"), "mat167 not loaded"
  assert pyDatalog.ask("subject('art310','humanities')"), "art310 not loaded"
  assert pyDatalog.ask("subject('his110','social science')"), "his110 not loaded"
  assert pyDatalog.ask("subject('psy150','social science')"), "psy150 not loaded"
  assert pyDatalog.ask("subject('eng101','humanities')"), "eng101 not loaded"

def test_2():
  """graduating students"""
  pyDatalog.clear()
  load_course_catalog()
  load_graduation_rules()
  
  assert_student_completed_class('s1', 'cs101')
  assert not ask_if_graduated('s1'), "student s1 should not have graduated yet"
  assert not ask_if_graduated('s2'), "student s2 should not have graduated yet"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert not find_graduates(), "no one should have graduated yet"
  
  assert_student_completed_class('s1', 'art310')
  assert not ask_if_graduated('s1'), "student s1 should not have graduated yet"
  assert not ask_if_graduated('s2'), "student s2 should not have graduated yet"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert not find_graduates(), "no one should have graduated yet"
  
  assert_student_completed_class('s1', 'eng101')
  assert not ask_if_graduated('s1'), "student s1 should not have graduated yet"
  assert not ask_if_graduated('s2'), "student s2 should not have graduated yet"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert not find_graduates(), "no one should have graduated yet"
  
  assert_student_completed_class('s1', 'psy150')
  print(pyDatalog.ask('completed(s1, X)'))
  print(pyDatalog.ask('subject(Z, Y)'))
  assert ask_if_graduated('s1'), "student s1 should have graduated"
  assert not ask_if_graduated('s2'), "student s2 should not have graduated yet"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert find_graduates() == {'s1'}, "only s1 should have graduated so far"
  
  assert_student_completed_class('s2', 'his110')
  assert ask_if_graduated('s1'), "student s1 should have graduated"
  assert not ask_if_graduated('s2'), "student s2 should not have graduated yet"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert find_graduates() == {'s1'}, "only s1 should have graduated so far"
  
  assert_student_completed_class('s2', 'eng101')
  assert ask_if_graduated('s1'), "student s1 should have graduated"
  assert not ask_if_graduated('s2'), "student s2 should not have graduated yet"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert find_graduates() == {'s1'}, "only s1 should have graduated so far"
  
  assert_student_completed_class('s3', 'mat167')
  assert ask_if_graduated('s1'), "student s1 should have graduated"
  assert not ask_if_graduated('s2'), "student s2 should not have graduated yet"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert find_graduates() == {'s1'}, "only s1 should have graduated so far"
  
  assert_student_completed_class('s2', 'mat167')
  assert ask_if_graduated('s1'), "student s1 should have graduated"
  assert ask_if_graduated('s2'), "student s2 should have graduated"
  assert not ask_if_graduated('s3'), "student s3 should not have graduated yet"
  assert find_graduates() == {'s1', 's2'}, "only s1 and s2 should have graduated so far"
  
  
if __name__ == '__main__':
    import pytest
    pytest.main()