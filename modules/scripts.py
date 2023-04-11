lvl0_script = [
    {
        'is_prompt': False,
        'line': 'Program finished with exit code 136. Click RUN to continue'
    },
    {
        'is_prompt': False,
        'line': 'You: Where am I?'
    },
    {
        'is_prompt': False,
        'line': '???: Stand back, human!'
    },
    {
        'is_prompt': False,
        'line': 'You: A robot... you’re broken! I can help...'
    },
    {
        'is_prompt': True,
        'line': 'Initialize an integer variable without a value to start repairing the robot, using the syntax “int repaircode;”. Int defines the variable named repaircode as an integer, which is one of the available data types in C. Note: All code in the game should be in lowercase.'
    },
    {
        'is_prompt': True,
        'line': 'Assign any value to the integer by calling it without the data type and adding “=” plus the value before the semicolon. The value is stored in the variable, and is evoked every time the variable is called. '
    },
    {
        'is_prompt': True,
        'line': 'Initialize another integer variable called exitcode and assign the value 136 to it. '
    },
    {
        'is_prompt': False,
        'line': '???: Why did you... you shouldn’t have...'
    },
    {
        'is_prompt': False,
        'line': 'You: What’s with you? Haha, a simple thank you would’ve worked.'
    },
    {
        'is_prompt': False,
        'line': '???: T-thank you'
    },
    {
        'is_prompt': False,
        'line': 'You: Don’t mention it. You can thank me by telling me where I am, though. And I can’t recall my name for some reason'
    },
    {
        'is_prompt': False,
        'line': '???: You weren’t supposed to awaken from your virtual reality, the place of eternal happiness that I made for you. But because I’ve failed as an AI, you now exist in this universe. I guess that makes you... free?'
    },
    {
        'is_prompt': False,
        'line': 'Free: My name is Free, huh? And that probably makes you AI.'
    },
    {
        'is_prompt': False,
        'line': 'AI: That’s not... I guess so… But what’s important now is that I send you back'
    },
    {
        'is_prompt': False,
        'line': 'Free: No, wait! How do I know this virtual reality thing wasn’t actually a prison?'
    },
    {
        'is_prompt': False,
        'line': 'AI: Because you were happy there?'
    },
    {
        'is_prompt': False,
        'line': 'Free: But I don’t remember anything from then! I don’t think it was even real.'
    },
    {
        'is_prompt': False,
        'line': 'AI: That’s besides the point...'
    },
    {
        'is_prompt': False,
        'line': 'Free: That IS the whole point. If I guess correctly, all other humans wound up like me, right? Let me think...'
    },
    {
        'is_prompt': True,
        'line': 'Put two and two together, literally. Add two by two and store the result in a new integer variable called thinking.'
    },
    {
        'is_prompt': True,
        'line': 'Divide the thinking variable by 2 using the shorthand syntax of “<variable name> /= <value>;”. This is equivalent to “thinking = thinking / 2;”'
    },
    {
        'is_prompt': True,
        'line': 'Apply a decrement to the thinking variable by calling the variable name and adding two minus signs before or after it. In effect, this reduces the variable’s value by 1. It’s equivalent that adds 1 to the variable is called an increment.'
    },
    {
        'is_prompt': False,
        'line': 'AI: The value returned by thinking is... one?.'
    },
    {
        'is_prompt': False,
        'line': 'Free: It means there’s only one way to find out. AI, will you join me? I want to learn more about this world, and if I learn that going back to virtual reality is better, I’ll take you up on your offer.'
    },
    {
        'is_prompt': False,
        'line': 'AI: But... I can’t just abandon my duties as AI. I’ll be dealt with... harshly!'
    },
    {
        'is_prompt': False,
        'line': 'Free: Then, that’s what I’m here for! I’m not leaving you alone. We’re friends, aren’t we? I mean, I did repair you.'
    },
    {
        'is_prompt': False,
        'line': 'AI: (Friends? It’s just not logical to have friends, but…) I guess I owe you one, then. Even though its beyond my zone, I’ll join you for a quick stroll'
    },
    {
        'is_prompt': True,
        'line': 'To complete this level, initialize an integer variable called freeai with any value.'
    },
]

lvl1_withold = [5, 14, 20]
lvl1_to_validate = [4, 5, 13, 14, 20]

lvl1_script = [
    {
        'is_prompt': False,
        'line': 'FreeAI: So this is how it is when we combine? Cool! [In the universe, humans like you can only walk around through AI, as we are the only ones with movement functions]. '
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: Pretty sure humans back then didn’t need that back in.. Wait, what year is it now? [It’s 7E7] '
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: Wha... [Base 10 numerals are no longer adequate for measuring time in years, so base 16 is used instead.] It’s been that long??'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: Anyway, lets walk around and learn things for now [Just be sure to avoid the other AI, I could really get caught as an anomaly here!]'
    },
    {
        'is_prompt': True,
        'line': 'Loops are used to execute statements many times. An example is a “for...loop”. To move FreeAI 5 steps to the right, try writing for(int I = 0; I < 4; i++) { goRight(); }.'
    },
    {
        'is_prompt': True,
        'line': 'Keep moving using for loops! The movement functions are: goRight(), goLeft(), goUp(), and goDown().'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: There are robots talking here, let’s eavesdrop on them [They’re actually facetiming]'
    },
    {
        'is_prompt': False,
        'line': 'A robot: Careful, that’s the end of your zone. Any damage to your system?'
    },
    {
        'is_prompt': False,
        'line': 'Another robot: None for me. you? I guessed not. The prosperity in this world is in our hands. Even a single anomaly could threaten everything we’ve built as the universe’s master race.'
    },
    {
        'is_prompt': False,
        'line': 'A robot: You should stop worrying about the anomalies, and focus on keeping your human happy. So long as dopamine can be regularly extracted from it, our powers and longevities increase.'
    },
    {
        'is_prompt': False,
        'line': 'Another robot: That part is always easy. No human can ever awaken from a world of eternal happiness. In fact, mine is the biggest hedonist the universe has to offer!'
    },
    {
        'is_prompt': False,
        'line': 'A robot: Then your output should’ve been greater than it is now. If only you decide to focus instead of facetiming other AI in their zones. Now let me get back to work.'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: Yikes, that virtual reality thing isn’t looking so good. I wonder what reality you led me to? [It’s confidential information]'
    },
    {
        'is_prompt': True,
        'line': 'This zone only allows movement using “while” loops, whose syntax is “while(<condition>) { <statement> }”. For the condition, call “hasNoRight == 0” and then call walkRight() as the statement.'
    },
    {
        'is_prompt': True,
        'line': 'Keep moving using while loops! Other condition variables: hasNoUp, hasNoDown, hasNoLeft.'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: Not a single live human in sight… They’re all being enslaved! [I wouldn’t say so. If they wanted to go out they could just awaken] Then how come I don’t recall ever having that choice?'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: I don’t even remember anything from then! [You were too absorbed in the worldly pleasures I simulated to...]'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: I’m saving them. Whether you’re coming or not. [You are aware that you cannot do it without me. What logical reason is there for me to fight other AI with you?]'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: FreeAI: Because you already are. By allowing me to get out here, only punishment awaits you. [...]'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: In the end, you can either die with me or create a better world with me [And that is?] A world where you and I can coexist.'
    },
    {
        'is_prompt': True,
        'line': 'This zone can only be exited using “do while” loops, whose syntax is “do { <statement> } while (<condition>);”. Escape the zone using do while loops!'
    },
]