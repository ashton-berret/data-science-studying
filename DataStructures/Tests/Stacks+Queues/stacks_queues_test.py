import sys
import os
import argparse
import traceback

def setup_imports():
    """Set up imports based on the command-line argument."""
    parser = argparse.ArgumentParser(description='Test stacks and queues operations')
    parser.add_argument('--mode', choices=['solution', 'practice'], default='solution',
                      help='Which implementation to test (solution or practice)')
    args = parser.parse_args()
  
    # Get the current directory and project root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir,'..', '..'))
    
    if args.mode == 'solution':
        # Import from Solutions
        solutions_dir = os.path.join(project_root, 'Solutions', 'Stacks+Queues')
        sys.path.insert(0, solutions_dir)
        print(f"Testing solution implementation from: {solutions_dir}")
    else:
        # Import from Practice
        practice_dir = os.path.join(project_root, 'Practice', 'Stacks+Queues')
        sys.path.insert(0, practice_dir)
        print(f"Testing practice implementation from: {practice_dir}")
     
# Setup the path and import
setup_imports()

try:
    from stacks_queues_operations import StackQueueOperations
except ImportError as e:
    print(f"❌ Could not import StackQueueOperations: {e}")
    print("Make sure the file exists in Solutions/Stacks+Queues/ or Practice/Stacks+Queues/")
    sys.exit(1)

def safe_test(test_name, test_func):
    """Wrapper to safely run tests with detailed error reporting"""
    print(f"\n{'='*60}")
    print(f"🧪 TESTING: {test_name}")
    print('='*60)
    
    try:
        test_func()
        print(f"✅ {test_name} - ALL TESTS PASSED!")
        return True
    except AssertionError as e:
        print(f"❌ {test_name} - ASSERTION FAILED:")
        print(f"   Error: {e}")
        print(f"   Location: {traceback.format_exc().splitlines()[-2].strip()}")
        return False
    except Exception as e:
        print(f"❌ {test_name} - UNEXPECTED ERROR:")
        print(f"   Error Type: {type(e).__name__}")
        print(f"   Error Message: {e}")
        print(f"   Full Traceback:")
        traceback.print_exc()
        return False

def test_array_stack():
    """Test ArrayStack implementation with detailed logging"""
    
    print("Step 1: Creating ArrayStack instance...")
    try:
        stack = StackQueueOperations.ArrayStack()
        print(f"   ✓ Stack created: {type(stack)}")
    except Exception as e:
        print(f"   ❌ Failed to create stack: {e}")
        raise
    
    print("\nStep 2: Testing empty stack state...")
    is_empty = stack.is_empty()
    size = stack.size()
    print(f"   is_empty() returned: {is_empty} (expected: True)")
    print(f"   size() returned: {size} (expected: 0)")
    assert is_empty == True, f"New stack should be empty, got is_empty={is_empty}"
    assert size == 0, f"New stack should have size 0, got size={size}"
    print("   ✓ Empty stack tests passed")
    
    print("\nStep 3: Testing push operations...")
    print("   Pushing 1...")
    stack.push(1)
    items_after_1 = getattr(stack, 'items', 'NO ITEMS ATTRIBUTE')
    print(f"   Stack state: {items_after_1}, size: {stack.size()}")
    
    print("   Pushing 2...")
    stack.push(2)
    items_after_2 = getattr(stack, 'items', 'NO ITEMS ATTRIBUTE')
    print(f"   Stack state: {items_after_2}, size: {stack.size()}")
    
    print("   Pushing 3...")
    stack.push(3)
    items_after_3 = getattr(stack, 'items', 'NO ITEMS ATTRIBUTE')
    print(f"   Stack state: {items_after_3}, size: {stack.size()}")
    
    size_after_pushes = stack.size()
    is_empty_after_pushes = stack.is_empty()
    print(f"   Final size: {size_after_pushes} (expected: 3)")
    print(f"   Final is_empty: {is_empty_after_pushes} (expected: False)")
    
    assert size_after_pushes == 3, f"Stack should have 3 elements, got {size_after_pushes}"
    assert is_empty_after_pushes == False, f"Stack should not be empty, got {is_empty_after_pushes}"
    print("   ✓ Push operations passed")
    
    print("\nStep 4: Testing peek operation...")
    peek_result = stack.peek()
    size_after_peek = stack.size()
    print(f"   peek() returned: {peek_result} (expected: 3)")
    print(f"   size after peek: {size_after_peek} (expected: 3)")
    print(f"   Stack state: {getattr(stack, 'items', 'NO ITEMS ATTRIBUTE')}")
    
    assert peek_result == 3, f"Top element should be 3, got {peek_result}"
    assert size_after_peek == 3, f"Peek should not change size, got {size_after_peek}"
    print("   ✓ Peek operation passed")
    
    print("\nStep 5: Testing pop operations...")
    print("   Popping first element...")
    pop1 = stack.pop()
    print(f"   pop() returned: {pop1} (expected: 3)")
    print(f"   Stack state: {getattr(stack, 'items', 'NO ITEMS ATTRIBUTE')}, size: {stack.size()}")
    assert pop1 == 3, f"Should pop 3, got {pop1}"
    
    print("   Popping second element...")
    pop2 = stack.pop()
    print(f"   pop() returned: {pop2} (expected: 2)")
    print(f"   Stack state: {getattr(stack, 'items', 'NO ITEMS ATTRIBUTE')}, size: {stack.size()}")
    assert pop2 == 2, f"Should pop 2, got {pop2}"
    
    size_after_two_pops = stack.size()
    assert size_after_two_pops == 1, f"Stack should have 1 element, got {size_after_two_pops}"
    
    print("   Popping final element...")
    pop3 = stack.pop()
    print(f"   pop() returned: {pop3} (expected: 1)")
    print(f"   Stack state: {getattr(stack, 'items', 'NO ITEMS ATTRIBUTE')}, size: {stack.size()}")
    assert pop3 == 1, f"Should pop 1, got {pop3}"
    
    final_is_empty = stack.is_empty()
    print(f"   Final is_empty: {final_is_empty} (expected: True)")
    assert final_is_empty == True, f"Stack should be empty after popping all, got {final_is_empty}"
    print("   ✓ Pop operations passed")
    
    print("\nStep 6: Testing exception handling...")
    print("   Testing pop from empty stack...")
    try:
        stack.pop()
        assert False, "Should raise IndexError when popping from empty stack"
    except IndexError as e:
        print(f"   ✓ Correctly raised IndexError: {e}")
    except Exception as e:
        assert False, f"Should raise IndexError, but got {type(e).__name__}: {e}"
    
    print("   Testing peek from empty stack...")
    try:
        stack.peek()
        assert False, "Should raise IndexError when peeking from empty stack"
    except IndexError as e:
        print(f"   ✓ Correctly raised IndexError: {e}")
    except Exception as e:
        assert False, f"Should raise IndexError, but got {type(e).__name__}: {e}"

def test_array_queue():
    """Test ArrayQueue implementation with detailed logging"""
    
    print("Step 1: Creating ArrayQueue instance...")
    try:
        queue = StackQueueOperations.ArrayQueue()
        print(f"   ✓ Queue created: {type(queue)}")
    except Exception as e:
        print(f"   ❌ Failed to create queue: {e}")
        raise
    
    print("\nStep 2: Testing empty queue state...")
    try:
        is_empty = queue.is_empty()
        size = queue.size()
        print(f"   is_empty() returned: {is_empty} (expected: True)")
        print(f"   size() returned: {size} (expected: 0)")
        assert is_empty == True, f"New queue should be empty, got is_empty={is_empty}"
        assert size == 0, f"New queue should have size 0, got size={size}"
        print("   ✓ Empty queue tests passed")
    except TypeError as e:
        print(f"   ❌ Method signature error: {e}")
        print("   🔍 This usually means you forgot 'self' parameter in method definition")
        raise
    
    print("\nStep 3: Testing enqueue operations...")
    print("   Enqueuing 1...")
    queue.enqueue(1)
    items_after_1 = getattr(queue, 'items', 'NO ITEMS ATTRIBUTE')
    print(f"   Queue state: {items_after_1}, size: {queue.size()}")
    
    print("   Enqueuing 2...")
    queue.enqueue(2)
    items_after_2 = getattr(queue, 'items', 'NO ITEMS ATTRIBUTE')
    print(f"   Queue state: {items_after_2}, size: {queue.size()}")
    
    print("   Enqueuing 3...")
    queue.enqueue(3)
    items_after_3 = getattr(queue, 'items', 'NO ITEMS ATTRIBUTE')
    print(f"   Queue state: {items_after_3}, size: {queue.size()}")
    
    size_after_enqueues = queue.size()
    is_empty_after_enqueues = queue.is_empty()
    print(f"   Final size: {size_after_enqueues} (expected: 3)")
    print(f"   Final is_empty: {is_empty_after_enqueues} (expected: False)")
    
    assert size_after_enqueues == 3, f"Queue should have 3 elements, got {size_after_enqueues}"
    assert is_empty_after_enqueues == False, f"Queue should not be empty, got {is_empty_after_enqueues}"
    print("   ✓ Enqueue operations passed")
    
    print("\nStep 4: Testing front operation...")
    front_result = queue.front()
    size_after_front = queue.size()
    print(f"   front() returned: {front_result} (expected: 1)")
    print(f"   size after front: {size_after_front} (expected: 3)")
    print(f"   Queue state: {getattr(queue, 'items', 'NO ITEMS ATTRIBUTE')}")
    
    assert front_result == 1, f"Front element should be 1, got {front_result}"
    assert size_after_front == 3, f"Front should not change size, got {size_after_front}"
    print("   ✓ Front operation passed")
    
    print("\nStep 5: Testing dequeue operations...")
    print("   Dequeuing first element...")
    dequeue1 = queue.dequeue()
    print(f"   dequeue() returned: {dequeue1} (expected: 1)")
    print(f"   Queue state: {getattr(queue, 'items', 'NO ITEMS ATTRIBUTE')}, size: {queue.size()}")
    assert dequeue1 == 1, f"Should dequeue 1, got {dequeue1}"
    
    print("   Dequeuing second element...")
    dequeue2 = queue.dequeue()
    print(f"   dequeue() returned: {dequeue2} (expected: 2)")
    print(f"   Queue state: {getattr(queue, 'items', 'NO ITEMS ATTRIBUTE')}, size: {queue.size()}")
    assert dequeue2 == 2, f"Should dequeue 2, got {dequeue2}"
    
    print("   Dequeuing final element...")
    dequeue3 = queue.dequeue()
    print(f"   dequeue() returned: {dequeue3} (expected: 3)")
    print(f"   Queue state: {getattr(queue, 'items', 'NO ITEMS ATTRIBUTE')}, size: {queue.size()}")
    assert dequeue3 == 3, f"Should dequeue 3, got {dequeue3}"
    
    final_is_empty = queue.is_empty()
    print(f"   Final is_empty: {final_is_empty} (expected: True)")
    assert final_is_empty == True, f"Queue should be empty after dequeuing all, got {final_is_empty}"
    print("   ✓ Dequeue operations passed")

def test_deque_queue():
    """Test DequeQueue implementation with detailed logging"""
    
    print("Step 1: Creating DequeQueue instance...")
    try:
        queue = StackQueueOperations.DequeQueue()
        print(f"   ✓ Queue created: {type(queue)}")
    except Exception as e:
        print(f"   ❌ Failed to create queue: {e}")
        raise
    
    print("\nStep 2: Testing empty queue state...")
    is_empty = queue.is_empty()
    size = queue.size()
    print(f"   is_empty() returned: {is_empty} (expected: True)")
    print(f"   size() returned: {size} (expected: 0)")
    assert is_empty == True, f"New queue should be empty, got is_empty={is_empty}"
    assert size == 0, f"New queue should have size 0, got size={size}"
    print("   ✓ Empty queue tests passed")
    
    print("\nStep 3: Testing enqueue operations...")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    size_after_enqueues = queue.size()
    is_empty_after_enqueues = queue.is_empty()
    print(f"   Size after enqueues: {size_after_enqueues} (expected: 3)")
    print(f"   is_empty after enqueues: {is_empty_after_enqueues} (expected: False)")
    
    assert size_after_enqueues == 3, f"Queue should have 3 elements, got {size_after_enqueues}"
    assert is_empty_after_enqueues == False, f"Queue should not be empty, got {is_empty_after_enqueues}"
    print("   ✓ Enqueue operations passed")
    
    print("\nStep 4: Testing front and rear operations...")
    front_result = queue.front()
    rear_result = queue.rear()
    size_after_peek = queue.size()
    print(f"   front() returned: {front_result} (expected: 1)")
    print(f"   rear() returned: {rear_result} (expected: 3)")
    print(f"   size after peek operations: {size_after_peek} (expected: 3)")
    
    assert front_result == 1, f"Front element should be 1, got {front_result}"
    assert rear_result == 3, f"Rear element should be 3, got {rear_result}"
    assert size_after_peek == 3, f"Peek operations should not change size, got {size_after_peek}"
    print("   ✓ Front and rear operations passed")
    
    print("\nStep 5: Testing dequeue operations...")
    dequeue1 = queue.dequeue()
    dequeue2 = queue.dequeue()
    dequeue3 = queue.dequeue()
    
    print(f"   First dequeue: {dequeue1} (expected: 1)")
    print(f"   Second dequeue: {dequeue2} (expected: 2)")
    print(f"   Third dequeue: {dequeue3} (expected: 3)")
    
    assert dequeue1 == 1, f"Should dequeue 1, got {dequeue1}"
    assert dequeue2 == 2, f"Should dequeue 2, got {dequeue2}"
    assert dequeue3 == 3, f"Should dequeue 3, got {dequeue3}"
    
    final_is_empty = queue.is_empty()
    assert final_is_empty == True, f"Queue should be empty after dequeuing all, got {final_is_empty}"
    print("   ✓ Dequeue operations passed")

def test_valid_parentheses():
    """Test valid_parentheses function with detailed logging"""
    
    print("Step 1: Testing valid parentheses cases...")
    valid_cases = [
        ("()", "simple parentheses"),
        ("()[]{}",  "multiple types"),
        ("{[]}", "nested brackets"),
        ("((()))", "multiple nested"),
        ("{[()]}", "complex nesting"),
        ("", "empty string")
    ]
    
    for test_case, description in valid_cases:
        print(f"   Testing '{test_case}' ({description})...")
        result = StackQueueOperations.valid_parentheses(test_case)
        print(f"   Result: {result} (expected: True)")
        assert result == True, f"'{test_case}' should be valid, got {result}"
    print("   ✓ All valid cases passed")
    
    print("\nStep 2: Testing invalid parentheses cases...")
    invalid_cases = [
        ("(", "unclosed opening"),
        (")", "unopened closing"),
        ("([)]", "interleaved"),
        ("(((", "multiple unclosed"),
        (")))", "multiple unopened"),
        ("{[}]", "wrong order"),
        ("([{})]", "complex wrong order")
    ]
    
    for test_case, description in invalid_cases:
        print(f"   Testing '{test_case}' ({description})...")
        result = StackQueueOperations.valid_parentheses(test_case)
        print(f"   Result: {result} (expected: False)")
        assert result == False, f"'{test_case}' should be invalid, got {result}"
    print("   ✓ All invalid cases passed")

def run_all_tests():
    """Run all test functions with detailed reporting"""
    print("🚀 STARTING COMPREHENSIVE STACKS AND QUEUES TESTS")
    print("="*70)
    
    tests = [
        ("ArrayStack", test_array_stack),
        ("DequeQueue", test_deque_queue), 
        ("ArrayQueue", test_array_queue),
        ("Valid Parentheses", test_valid_parentheses),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        if safe_test(test_name, test_func):
            passed += 1
        else:
            failed += 1
    
    print(f"\n{'='*70}")
    print(f"📊 FINAL RESULTS:")
    print(f"   ✅ Passed: {passed}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📈 Success Rate: {passed}/{passed + failed} ({100 * passed / (passed + failed):.1f}%)")
    
    if failed == 0:
        print("🎉 ALL TESTS PASSED! Your implementation is working correctly!")
    else:
        print("🔧 Some tests failed. Check the detailed output above to fix the issues.")
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 
