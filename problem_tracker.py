#!/usr/bin/env python3
"""
Problem Tracker and Random Generator

Usage:
    python problem_tracker.py list                    # Show all categories and problems
    python problem_tracker.py random arrays           # Get random array problem
    python problem_tracker.py random                  # Get random problem from any category
    python problem_tracker.py stats                   # Show practice statistics
    python problem_tracker.py add arrays "Two Sum"    # Add new problem (optional)
"""

import os
import sys
import json
import random
import argparse
from datetime import datetime
from pathlib import Path

class ProblemTracker:
    def __init__(self, base_dir=None):
        """Initialize the problem tracker"""
        if base_dir is None:
            # Try to find the DataStructures directory
            current = Path.cwd()
            while current != current.parent:
                if (current / "DataStructures").exists():
                    base_dir = current / "DataStructures"
                    break
                current = current.parent
            else:
                base_dir = Path.cwd()
        
        self.base_dir = Path(base_dir)
        self.data_file = self.base_dir / "problem_tracker.json"
        self.stats_file = self.base_dir / "practice_stats.json"
        
        # Initialize problem database
        self.problems = self._load_problems()
        self.stats = self._load_stats()
    
    def _load_problems(self):
        """Load problems from file or create default database"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                return json.load(f)
        else:
            # Create default problem database based on what we've implemented
            default_problems = {
                "arrays": {
                    "description": "Array manipulation and searching algorithms",
                    "problems": [
                        {
                            "name": "Two Sum",
                            "difficulty": "Easy",
                            "description": "Find two numbers that add up to target",
                            "file": "arrays_operations.py",
                            "method": "two_sum"
                        },
                        {
                            "name": "Binary Search",
                            "difficulty": "Easy", 
                            "description": "Search for target in sorted array",
                            "file": "arrays_operations.py",
                            "method": "binary_search"
                        },
                        {
                            "name": "Merge Sorted Arrays",
                            "difficulty": "Easy",
                            "description": "Merge two sorted arrays in-place",
                            "file": "arrays_operations.py", 
                            "method": "merge_sorted_arrays"
                        },
                        {
                            "name": "Remove Duplicates",
                            "difficulty": "Easy",
                            "description": "Remove duplicates from sorted array in-place",
                            "file": "arrays_operations.py",
                            "method": "remove_duplicates"
                        },
                        {
                            "name": "Search Insert Position", 
                            "difficulty": "Easy",
                            "description": "Find position where target should be inserted",
                            "file": "arrays_operations.py",
                            "method": "search_insert_position"
                        },
                        {
                            "name": "First and Last Position",
                            "difficulty": "Medium", 
                            "description": "Find first and last position of target in sorted array",
                            "file": "arrays_operations.py",
                            "method": "find_first_and_last_position"
                        },
                        {
                            "name": "Linear Search",
                            "difficulty": "Easy",
                            "description": "Find the index of a target element in an unsorted array",
                            "file": "arrays_operations.py",
                            "method": "find_element"
                        },
                        {
                            "name": "Find Maximum and Minimum",
                            "difficulty": "Easy",
                            "description": "Find both the maximum and minimum elements in array in a single pass.",
                            "file": "arrays_operations.py",
                            "method": "find_min_max"
                        },
                        {
                            "name": "Kadane's Algorithm with Indices",
                            "difficulty": "Medium",
                            "description": "Find the maximum sum subarray and return both the sum and the start/end indices of the subarray.",
                            "file": "arrays_operations.py",
                            "method": "kadanes_with_subarray"
                        }
                    ]
                },
                "sliding_window": {
                    "description": "Sliding window pattern problems",
                    "problems": [
                        {
                            "name": "Maximum Subarray Sum",
                            "difficulty": "Easy",
                            "description": "Find maximum sum of k consecutive elements",
                            "file": "sliding_window_operations.py",
                            "method": "max_sum_subarray_of_size_k"
                        },
                        {
                            "name": "Minimum Subarray Sum",
                            "difficulty": "Easy",
                            "description": "Find the minimal length of a contiguous subarray whose sum is greater than or equal to the target.",
                            "file": "sliding_window_operations.py",
                            "method": "smallest_subarray_with_given_sum"
                        },
                        {
                            "name": "Longest Substring Without Repeating",
                            "difficulty": "Medium",
                            "description": "Find length of longest substring without repeating characters",
                            "file": "sliding_window_operations.py", 
                            "method": "length_of_longest_substring"
                        },
                        {
                            "name": "Longest Substring with K distincts",
                            "difficulty": "Medium",
                            "description": "Find the lenght of the longest substring that contains at most k distinct characters",
                            "file": "sliding_window_operations.py",
                            "method": "longest_substring_with_k_distinct"
                        },
                        {
                            "name": "Fruits into Baskets",
                            "difficulty": "Medium",
                            "description": "Pick fruits from trees in baskets (one fruit type per basket). Find the maximum number of fruits you can collect with two baskets",
                            "file": "sliding_window_operations.py",
                            "method": "fruits_into_baskets"
                        },
                        {
                            "name": "Find all anagrams",
                            "difficulty": "Medium",
                            "description": "Given two strings, return an array of all the start indices of s1's anagrams in s2",
                            "file": "sliding_window_operations.py",
                            "method": "find_all_anagrams"
                        },
                        {
                            "name": "Longest Repeating Character Replacement",
                            "difficulty": "Medium",
                            "description": "Find the length of the longest substring with the same characters after replacing at most k characters.",
                            "file": "sliding_window_operations.py",
                            "method": "longest_repeating_character_replacement"
                        },
                        {
                            "name": "Minimum Window Substring",
                            "difficulty": "Hard",
                            "description": "Find minimum window containing all characters of pattern",
                            "file": "sliding_window_operations.py",
                            "method": "min_window_substring"
                        },
                        {
                            "name": "Sliding Window Maximum",
                            "difficulty": "Hard", 
                            "description": "Find maximum in each sliding window of size k",
                            "file": "sliding_window_operations.py",
                            "method": "sliding_window_maximum"
                        },
                        {
                            "name": "Permutation in String",
                            "difficulty": "Medium",
                            "description": "Check if string contains permutation of pattern",
                            "file": "sliding_window_operations.py",
                            "method": "check_inclusion"
                        }
                    ]
                },
                "hashmaps": {
                    "description": "HashMap and HashSet problems",
                    "problems": [
                        {
                            "name": "Valid Anagram",
                            "difficulty": "Easy",
                            "description": "Check if two strings are anagrams",
                            "file": "hashmap_operations.py",
                            "method": "is_anagram"
                        },
                        {
                            "name": "Group Anagrams", 
                            "difficulty": "Medium",
                            "description": "Group strings that are anagrams of each other",
                            "file": "hashmap_operations.py",
                            "method": "group_anagrams"
                        },
                        {
                            "name": "Top K Frequent Elements",
                            "difficulty": "Medium",
                            "description": "Find k most frequent elements in array",
                            "file": "hashmap_operations.py",
                            "method": "top_k_frequent"
                        },
                        {
                            "name": "Intersection of Arrays",
                            "difficulty": "Easy",
                            "description": "Find intersection of two arrays",
                            "file": "hashmap_operations.py", 
                            "method": "intersection"
                        },
                        {
                            "name": "Contains Duplicate",
                            "difficulty": "Easy",
                            "description": "Check if array contains duplicates",
                            "file": "hashmap_operations.py",
                            "method": "contains_duplicate"
                        },
                        {
                            "name": "Find all duplicates",
                            "difficulty": "Medium",
                            "description": "Find all the elements that appear twice in an array",
                            "file": "hashmap_operations.py",
                            "method": "find_all_duplicates"
                        },
                        {
                            "name": "Union of Arrays",
                            "difficulty": "Easy",
                            "description": "Find the union of two arrays (all unique elements)",
                            "file": "hashmap_operations.py",
                            "method": "union_of_arrays"
                        },
                        {
                            "name": "Character Frequency Count",
                            "difficulty": "Easy",
                            "description": "Count the frequency of each character in a string and return as a hashmap",
                            "file": "hashmap_operations.py",
                            "method": "character_frequency"
                        },
                        {
                            "name": "First Non-Repeating Character",
                            "difficulty": "Easy",
                            "description": "Find the first character in a string that doesn't repeat. Return its index or -1",
                            "file": "hashmap_operations.py",
                            "method": "first_non_repeating_character"
                        },
                        {
                            "name": "Longest Consecutive Sequence",
                            "difficulty": "Medium",
                            "description": "Find length of longest consecutive sequence",
                            "file": "hashmap_operations.py",
                            "method": "longest_consecutive"
                        },
                        {
                            "name": "Subarray Sum Equals K",
                            "difficulty": "Medium",
                            "description": "Find the total number of continuous subarrays whose sum equals k",
                            "file": "hashmap_operations.py",
                            "method": "subarray_sum_equals_k"
                        },
                        {
                            "name": "4SumII",
                            "difficulty": "Medium",
                            "description": "Given four arrays, count tuples (i, j, k, l) such that A[i] + B[j] + C[k] + D[l] = 0",
                            "file": "hashmap_operations.py",
                            "method": "four_sum_count"
                        },
                        {
                            "name": "Valid Sudoku",
                            "difficulty": "Medium",
                            "description": "Determine if a 9x9 sudoku board is valid (partially filled, checking existing numbers only)",
                            "file": "hashmap_operations.py",
                            "method": "valid_sudoku"
                        }
                    ]
                },
                "stacks_queues": {
                    "description": "Stack and Queue problems",
                    "problems": [
                        {
                            "name": "Valid Parentheses",
                            "difficulty": "Easy", 
                            "description": "Check if parentheses are properly balanced",
                            "file": "stacks_queues_operations.py",
                            "method": "valid_parentheses"
                        },
                        {
                            "name": "Daily Temperatures",
                            "difficulty": "Medium",
                            "description": "Find days until warmer temperature",
                            "file": "stacks_queues_operations.py",
                            "method": "daily_temperatures" 
                        },
                        {
                            "name": "Evaluate Postfix Expression",
                            "difficulty": "Medium",
                            "description": "Evaluate postfix mathematical expression",
                            "file": "stacks_queues_operations.py",
                            "method": "evaluate_postfix"
                        },
                        {
                            "name": "Implement Stack with Queues",
                            "difficulty": "Easy",
                            "description": "Implement stack using only queue operations",
                            "file": "stacks_queues_operations.py",
                            "method": "implement_stack_using_queues"
                        },
                        {
                            "name": "Implement Queue with Stacks", 
                            "difficulty": "Easy",
                            "description": "Implement queue using only stack operations",
                            "file": "stacks_queues_operations.py",
                            "method": "implement_queue_using_stacks"
                        },
                        {
                            "name": "Sliding Window Maximum",
                            "difficulty": "Hard",
                            "description": "Find maximum in sliding window using deque",
                            "file": "stacks_queues_operations.py",
                            "method": "sliding_window_maximum"
                        },
                        {
                            "name": "First Negative in Window",
                            "difficulty": "Easy",
                            "description": "Find the first negative number in every window of size k in an array",
                            "file": "stacks_queues_operations.py",
                            "method": "first_negative_in_window"
                        }
                    ]
                },
                "linked_lists": {
                    "description": "Linked List manipulation problems", 
                    "problems": [
                        {
                            "name": "Reverse Linked List",
                            "difficulty": "Easy",
                            "description": "Reverse a singly linked list",
                            "file": "linked_lists_operations.py",
                            "method": "reverse_linked_list"
                        },
                        {
                            "name": "Find Middle Node",
                            "difficulty": "Easy",
                            "description": "Find the middle node of a linked list. If even, return the second middle node",
                            "file": "linked_lists_operations.py",
                            "method": "find_middle_node"
                        },
                        {
                            "name": "Linked List Cycle Detection",
                            "difficulty": "Easy", 
                            "description": "Detect if linked list has a cycle",
                            "file": "linked_lists_operations.py",
                            "method": "has_cycle"
                        },
                        {
                            "name": "Find Cycle Start",
                            "difficulty": "Medium",
                            "description": "Find where cycle begins in linked list",
                            "file": "linked_lists_operations.py",
                            "method": "find_cycle_start"
                        },
                        {
                            "name": "Merge Two Sorted Lists",
                            "difficulty": "Easy",
                            "description": "Merge two sorted linked lists",
                            "file": "linked_lists_operations.py",
                            "method": "merge_two_sorted_lists"
                        },
                        {
                            "name": "Remove Duplicates from Sorted List",
                            "difficulty": "Easy",
                            "description": "Remove duplicate nodes from a sorted list, keeping only unique values",
                            "file": "linked_lists_operations.py",
                            "method":"remove_duplicates_sorted"
                        },
                        {
                            "name": "Remove Nth From End",
                            "difficulty": "Medium", 
                            "description": "Remove nth node from end of list",
                            "file": "linked_lists_operations.py",
                            "method": "remove_nth_from_end"
                        },
                        {
                            "name": "Palindrome Linked List",
                            "difficulty": "Easy",
                            "description": "Check if linked list is palindrome",
                            "file": "linked_lists_operations.py",
                            "method": "is_palindrome"
                        },
                        {
                            "name": "Add Two Numbers",
                            "difficulty": "Medium",
                            "description": "Add numbers represented as linked lists",
                            "file": "linked_lists_operations.py", 
                            "method": "add_two_numbers"
                        },
                        {
                            "name": "Intersection of Two Lists",
                            "difficulty": "Easy",
                            "description": "Find intersection point of two linked lists",
                            "file": "linked_lists_operations.py",
                            "method": "intersection_of_two_lists"
                        },
                        {
                            "name": "Partition List",
                            "difficulty": "Medium",
                            "description": "Partition a linked list around value x, with all nodes < x before nodes >= x",
                            "file": "linked_lists_operations.py",
                            "method": "partition_list"
                        }
                    ]
                }
            }
            self._save_problems(default_problems)
            return default_problems
    
    def _load_stats(self):
        """Load practice statistics"""
        if self.stats_file.exists():
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        else:
            return {
                "total_problems_solved": 0,
                "problems_by_category": {},
                "problems_by_difficulty": {"Easy": 0, "Medium": 0, "Hard": 0},
                "last_practiced": {},
                "practice_streak": 0,
                "last_practice_date": None
            }
    
    def _save_problems(self, problems=None):
        """Save problems to file"""
        if problems is None:
            problems = self.problems
        with open(self.data_file, 'w') as f:
            json.dump(problems, f, indent=2)
    
    def _save_stats(self):
        """Save statistics to file"""
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=2)
    
    def list_all_problems(self):
        """Display all categories and problems"""
        print("📚 AVAILABLE PROBLEMS BY CATEGORY")
        print("=" * 60)
        
        total_problems = 0
        for category, data in self.problems.items():
            print(f"\n🔸 {category.upper().replace('_', ' ')}")
            print(f"   {data['description']}")
            print("   " + "-" * 50)
            
            for i, problem in enumerate(data['problems'], 1):
                difficulty_emoji = {
                    "Easy": "🟢",
                    "Medium": "🟡", 
                    "Hard": "🔴"
                }
                emoji = difficulty_emoji.get(problem['difficulty'], "⚪")
                
                print(f"   {i:2d}. {emoji} {problem['name']} ({problem['difficulty']})")
                print(f"       {problem['description']}")
            
            total_problems += len(data['problems'])
        
        print(f"\n📊 SUMMARY: {total_problems} total problems across {len(self.problems)} categories")
    
    def get_random_problem(self, category=None, difficulty=None):
        """Get a random problem, optionally filtered by category and/or difficulty"""
        eligible_problems = []
        
        categories_to_search = [category] if category else self.problems.keys()
        
        for cat in categories_to_search:
            if cat not in self.problems:
                print(f"❌ Category '{cat}' not found!")
                return None
            
            for problem in self.problems[cat]['problems']:
                if difficulty is None or problem['difficulty'].lower() == difficulty.lower():
                    problem_info = problem.copy()
                    problem_info['category'] = cat
                    eligible_problems.append(problem_info)
        
        if not eligible_problems:
            print("❌ No problems found matching your criteria!")
            return None
        
        selected = random.choice(eligible_problems)
        self._display_problem(selected)
        return selected
    
    def _display_problem(self, problem):
        """Display a problem in a nice format"""
        difficulty_emoji = {
            "Easy": "🟢",
            "Medium": "🟡",
            "Hard": "🔴"
        }
        emoji = difficulty_emoji.get(problem['difficulty'], "⚪")
        
        print("\n" + "=" * 60)
        print(f"🎯 RANDOM PROBLEM SELECTED!")
        print("=" * 60)
        print(f"📂 Category: {problem['category'].replace('_', ' ').title()}")
        print(f"{emoji} Problem: {problem['name']} ({problem['difficulty']})")
        print(f"📝 Description: {problem['description']}")
        print(f"📁 File: {problem['file']}")
        print(f"⚙️  Method: {problem['method']}")
        
        # Show file path with directory name handling
        category_dir_map = {
            'stacks_queues': 'Stacks+Queues',
            'hashmaps': 'Hashmap+Sets',
            'sliding_window': 'SlidingWindow+TwoPointer',
            'linked_lists': 'Linked Lists',
            'arrays': 'Arrays'
        }
        dir_name = category_dir_map.get(problem['category'], problem['category'].replace('_', ' ').title())
        practice_path = self.base_dir / "Practice" / dir_name / problem['file']
        solutions_path = self.base_dir / "Solutions" / dir_name / problem['file']
        
        print(f"\n📂 PRACTICE FILES:")
        if practice_path.exists():
            print(f"   🔧 Practice: {practice_path}")
        else:
            print(f"   ⚠️  Practice file not found: {practice_path}")
        
        if solutions_path.exists():
            print(f"   ✅ Solution: {solutions_path}")
        else:
            print(f"   ⚠️  Solution file not found: {solutions_path}")
        
        print("\n🚀 NEXT STEPS:")
        print("   1. Open the practice file")
        print("   2. Implement the solution")
        print("   3. Run tests to verify")
        print("   4. Compare with solution if needed")
        print("=" * 60)
    
    def show_stats(self):
        """Display practice statistics"""
        print("\n📊 PRACTICE STATISTICS")
        print("=" * 50)
        
        print(f"🎯 Total Problems Solved: {self.stats['total_problems_solved']}")
        print(f"🔥 Current Streak: {self.stats['practice_streak']} days")
        
        if self.stats['last_practice_date']:
            print(f"📅 Last Practice: {self.stats['last_practice_date']}")
        
        print(f"\n📈 BY DIFFICULTY:")
        for difficulty, count in self.stats['problems_by_difficulty'].items():
            emoji = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}[difficulty]
            print(f"   {emoji} {difficulty}: {count}")
        
        print(f"\n📂 BY CATEGORY:")
        for category, count in self.stats['problems_by_category'].items():
            print(f"   🔸 {category.replace('_', ' ').title()}: {count}")
        
        # Show recently practiced
        if self.stats['last_practiced']:
            print(f"\n🕒 RECENTLY PRACTICED:")
            recent_items = sorted(
                self.stats['last_practiced'].items(),
                key=lambda x: x[1],
                reverse=True
            )[:5]
            for problem, date in recent_items:
                print(f"   • {problem} - {date}")
    
    def mark_completed(self, category, problem_name):
        """Mark a problem as completed (for manual tracking)"""
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Update stats
        self.stats['total_problems_solved'] += 1
        self.stats['problems_by_category'][category] = self.stats['problems_by_category'].get(category, 0) + 1
        
        # Find difficulty
        if category in self.problems:
            for problem in self.problems[category]['problems']:
                if problem['name'].lower() == problem_name.lower():
                    difficulty = problem['difficulty']
                    self.stats['problems_by_difficulty'][difficulty] += 1
                    break
        
        self.stats['last_practiced'][f"{category}:{problem_name}"] = today
        self.stats['last_practice_date'] = today
        
        # Update streak
        # Simple implementation - just increment for now
        self.stats['practice_streak'] += 1
        
        self._save_stats()
        print(f"✅ Marked '{problem_name}' from {category} as completed!")
    
    def add_problem(self, category, name, difficulty="Medium", description=""):
        """Add a new problem to the database"""
        if category not in self.problems:
            self.problems[category] = {
                "description": f"{category.replace('_', ' ').title()} problems",
                "problems": []
            }
        
        new_problem = {
            "name": name,
            "difficulty": difficulty,
            "description": description or f"Practice {name}",
            "file": f"{category}_operations.py",
            "method": name.lower().replace(' ', '_')
        }
        
        self.problems[category]['problems'].append(new_problem)
        self._save_problems()
        print(f"✅ Added '{name}' to {category} category!")

def main():
    parser = argparse.ArgumentParser(
        description="Problem Tracker and Random Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python problem_tracker.py list                    # Show all problems
  python problem_tracker.py random                  # Random problem from any category  
  python problem_tracker.py random arrays           # Random array problem
  python problem_tracker.py random arrays easy      # Random easy array problem
  python problem_tracker.py stats                   # Show statistics
  python problem_tracker.py complete arrays "Two Sum"  # Mark problem as completed
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    subparsers.add_parser('list', help='List all problems')
    
    # Random command
    random_parser = subparsers.add_parser('random', help='Get random problem')
    random_parser.add_argument('category', nargs='?', help='Category filter (optional)')
    random_parser.add_argument('difficulty', nargs='?', help='Difficulty filter (optional)')
    
    # Stats command
    subparsers.add_parser('stats', help='Show practice statistics')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark problem as completed')
    complete_parser.add_argument('category', help='Problem category')
    complete_parser.add_argument('problem', help='Problem name')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add new problem')
    add_parser.add_argument('category', help='Category name')
    add_parser.add_argument('name', help='Problem name')
    add_parser.add_argument('--difficulty', default='Medium', help='Problem difficulty')
    add_parser.add_argument('--description', default='', help='Problem description')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    tracker = ProblemTracker()
    
    if args.command == 'list':
        tracker.list_all_problems()
    
    elif args.command == 'random':
        tracker.get_random_problem(args.category, args.difficulty)
    
    elif args.command == 'stats':
        tracker.show_stats()
    
    elif args.command == 'complete':
        tracker.mark_completed(args.category, args.problem)
    
    elif args.command == 'add':
        tracker.add_problem(args.category, args.name, args.difficulty, args.description)

if __name__ == "__main__":
    main() 
