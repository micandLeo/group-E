# analysis.py: Calculate SUS (System Usability Scale) score
# HCI Coursework Group-E
def calculate_sus(scores):
    """
    Input: list of 10 integer ratings (1~5)
    Return: final SUS score 0~100
    SUS rule:
    Odd items(1,3,5,7,9): score = value - 1
    Even items(2,4,6,8,10): score = 5 - value
    Sum all, multiply by 2.5
    """
    if len(scores) != 10:
        raise ValueError("Must input exactly 10 SUS ratings!")
    total = 0
    for idx, val in enumerate(scores):
        item_number = idx + 1
        if item_number % 2 == 1:
            total += val - 1
        else:
            total += 5 - val
    return total * 2.5

if __name__ == "__main__":
    participant1 = [4,4,3,2,2,4,2,4,2,3]
    p1_score = calculate_sus(participant1)
    print(f"Participant 1 SUS score: {p1_score}")

    participant2 = [3,4,4,2,1,4,2,3,1,4]
    p2_score = calculate_sus(participant2)
    print(f"Participant 2 SUS score: {p2_score}")
