// 合并K个升序链表
// Merge k Sorted Lists

#include "common.h"

class Solution
{
public:
    ListNode *mergeKLists(std::vector<ListNode *> &lists)
    {
        if (lists.empty()) {
            return nullptr;
        }
        return mergeIndex(lists, 0, lists.size() - 1);
    }

    ListNode *mergeIndex(std::vector<ListNode *> &lists, int leftIndex, int rightIndex)
    {
        if (leftIndex == rightIndex)
        {
            return lists[leftIndex];
        }

        int midIndx = leftIndex + (rightIndex - leftIndex) / 2;

        return merge(mergeIndex(lists, leftIndex, midIndx), mergeIndex(lists, midIndx + 1, rightIndex));
    }

    ListNode *merge(ListNode *left, ListNode *right)
    {
        ListNode dummy_head(0);
        ListNode *curr = &dummy_head;

        while (left && right)
        {
            if (left->val <= right->val)
            {
                curr->next = left;
                left = left->next;
            }
            else
            {
                curr->next = right;
                right = right->next;
            }
            curr = curr->next;
        }

        curr->next = left ? left : right;

        return dummy_head.next;
    }
};

int main()
{
    std::vector<std::vector<std::vector<int>>> test_cases = {
        {{1, 4, 5}, {1, 3, 4}, {2, 6}},
        {},
        {{}},
        {{}, {-2}, {-3, -2, -1}},
    };

    for (const auto &lists : test_cases)
    {
        std::vector<ListNode *> heads;
        for (const auto &arr : lists)
        {
            heads.push_back(create_linked_list(arr));
        }
        print_linked_list(Solution().mergeKLists(heads));
    }
}
