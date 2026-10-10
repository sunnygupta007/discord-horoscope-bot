from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'hey' in lowered:
        return 'Heyy there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'sorry' in lowered:
        return 'Its okay. I am kind hearted 😊'
    elif 'no' in lowered:
        return 'Someone has to do it buddy, that\'s the rule of the life 🫠'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 12)}'
    else:
        return choice(["I do not understand...",
                        "What are you talking about?",
                        "Are you trying to annoy me? 😑 I do have feelings",
                        "Do you mind rephrasing that?",
                        "Could you clarify?",
                        "I'm not quite following. Could you elaborate?",
                        "That's unclear. Can you provide more context?",
                        "I'm sorry, I'm having trouble grasping that.",
                        "It seems I'm missing something. Can you explain further?",
                        "I'm not sure I understand. Could you simplify?",
                        "I'm having difficulty comprehending. Can you clarify?"
                        ])
