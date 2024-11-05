// 排序链表
// Sort List

#include "common.h"

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }

        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* right = slow->next;
        slow->next = nullptr;
        ListNode* left = head;

        return merge(sortList(left), sortList(right));
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        ListNode dummy_head(0);
        ListNode* curr = &dummy_head;

        while (left && right) {
            if (left->val <= right->val) {
                curr->next = left;
                left = left->next;
            } else {
                curr->next = right;
                right = right->next;
            }
            curr = curr->next;
        }

        curr->next = left ? left : right;

        return dummy_head.next;
    }
};

int main() {
    std::vector<std::vector<int>> test_cases = {
        {4, 2, 1, 3},
        {-1, 5, 3, 4, 0},
        {},
    };

    for (const auto &arr : test_cases)
    {
        ListNode* head = create_linked_list(arr);
        print_linked_list(Solution().sortList(head));
    }
    return 0;
}

