// 环形链表
// Linked List Cycle

#include "common.h"

#include <iostream>

class Solution
{
public:
    bool hasCycle(ListNode *head)
    {
        if (head == nullptr || head->next == nullptr)
        {
            return false;
        }

        ListNode *slow = head;
        ListNode *fast = head;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast)
            {
                return true;
            }
        }

        return false;
    }
};

int main()
{
    std::vector<std::tuple<std::vector<int>, int>> test_cases = {
        {{3, 2, 0, -4}, 1},
        {{1, 2}, 0},
        {{1}, -1},
    };

    for (const auto &[arr, pos] : test_cases)
    {
        ListNode *head = create_linked_list(arr);
        print_linked_list(head);
        ListNode *head_cycle = create_cycle_linked_list(arr, pos);
        std::cout << Solution().hasCycle(head_cycle) << std::endl;
    }
    return 0;
}
