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
        'line': 'This zone only allows movement using “while” loops, whose syntax is “while(<condition>) { <statement> }”. For the condition, call “hasNoRight == 0” and then call goRight() as the statement.'
    },
    {
        'is_prompt': True,
        'line': 'Keep moving using while loops! Other condition variables: hasNoUp, hasNoDown, hasNoLeft. Note: Dont bump into other robots!'
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

lvl2_withold = [4, 9, 18]
lvl2_to_validate = [4, 6, 9, 13, 18, 21]

lvl2_script = [
    {
        'is_prompt': False,
        'line': 'FreeAI: So, how does fighting work in this world? [It’s a simple battle between three elementoids: the electroids, wateroids, and firoids, where the one before beats the one after, and firoids beat electroids.]'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: And how do I use these “elementoids”? [We’ll predict what elementoid the opponent uses and program our response with control structures] Hmmm, okay. Now let’s free some humans!'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: [An “if” statement has a syntax of “if (<condition>) {<statements>}”, an “if...else” statement has an additional “else {<statements>}”, while and “if...else if...else” statement has extra “else if (<condition>) {<statements>}” in between].'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: [In this case, set the condition to “turnNum == 1” for the first turn, and the statement to either useElectroid(), useWateroid(), or useFiroid(). To start a fight, just move closer to an enemy]'
    },
    {
        'is_prompt': True,
        'line': 'This zone only supports movement with while loops.'
    },
    {
        'is_prompt': False,
        'line': 'A robot: An anomaly! And that’s... a live human?? I’ll subdue this threat!'
    },
    {
        'is_prompt': True,
        'line': 'FreeAI’s prediction about the opponent’s attack/s yielded the following results: Turn 1: useFiroid(). Write a control structure that counters this.'
    },
    {
        'is_prompt': False,
        'line': 'A robot: Why… are you… working with that thi...'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: Did we… kill them both? [No, the AI just ran out of power. If you want to have enough time to free the human inside, we should beat the others first]'
    },
    {
        'is_prompt': True,
        'line': 'Continue moving using while loops.'
    },
    {
        'is_prompt': False,
        'line': 'Another robot: It’s the first time I’ve seen a human’s life spared by an anomaly. The most logical thing to do would’ve been to eliminate it, but I guess this AI has lost its mind.'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: We don’t have to fight. We just want to see if your human is alive.'
    },
    {
        'is_prompt': False,
        'line': 'Another robot: No, we do. My calculations are complete – and they tell me you should perish!'
    },
    {
        'is_prompt': True,
        'line': 'FreeAI’s prediction about the opponent’s attack/s yielded the following results: Turn 1: useWateroid(), All other turns: useElectroid()'
    },
    {
        'is_prompt': False,
        'line': 'Another robot: This can’t be! My calculations are absolute!'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: That wasn’t necessary at all. Can AI actually think for itself, or? [We base our judgements independent of emotion. The emotion...based decisions of humans caused ruin to the world, after all]'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: But purely logical decisions miss the point, too. He would’ve realized that we meant no harm. [But the risk of letting an anomaly, with a human, loose outweighs the possibility that we mean no harm, hence his calculation]'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: A world with no heart... that’s not a world I’d want to live in'
    },
    {
        'is_prompt': True,
        'line': 'Continue moving using while loops.'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: I know what this looks like, but if you could just give us a second to expl...'
    },
    {
        'is_prompt': False,
        'line': 'Yet another robot: Exterminate!'
    },
    {
        'is_prompt': True,
        'line': 'FreeAI’s prediction about the opponent’s attack/s yielded the following results: Turn 70: useElectroid(), Turn 421: useFiroid(), All other turns: useWateroid()'
    },
    {
        'is_prompt': False,
        'line': 'Yet another robot: Terminate my system. I no longer have a purpose, now that I have failed my duty.'
    },
    {
        'is_prompt': False,
        'line': 'FreeAI: You still do, and we’ll prove it to you. We won’t just save the humans inside, but the AI too!'
    },
]