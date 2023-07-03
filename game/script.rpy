# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define reader = Character(_("You"), color = "#68eebb")
define narrator = Character(_("Narrator"), color = "#ee689b")
define iris = Character(_("Iris"), color = "#74d9ed")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg one

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    narrator "The soft tapping of footsteps behind me - they serve as the only 
    indication that I'm not walking alone. I turn my head to look at the girl 
    beside me … just in time to catch her stealing a furtive glance at me." 
    
    narrator " ... That girl is Iris, a good friend of mine and neighbor since
    we were children. We 
    always take the bus back from school and walk home together, but today she 
    was being uncharacteristically quiet. I had already resigned myself to her 
    silent company, when I hear her footsteps suddenly stop."

    show mc normal

    reader "What's wrong?"

    hide mc normal
    show iris normal

    iris "... It's college decision day and you still haven't told anyone what 
    your plans after high school are."

    narrator "Iris frowns, crossing her arms and sticking out her bottom lip 
    dramatically."

    hide iris normal
    show mc normal

    reader "Oh, I'm planning on continuing my education in Kanagawa."

    hide mc normal
    show iris normal

    iris "I see, I thought that might be the case."

    narrator "Her tone is clearly dejected. Her eyes avert my gaze."

    hide iris normal
    show mc normal

    reader "Why do you say that?"

    hide mc normal
    show iris normal

    iris "You always seem like you want to go far away from here, for some 
    reason ..."

    hide iris normal
    show mc normal

    narrator "..." 

    reader "What about you, Iris?"

    hide mc normal
    show iris normal

    iris "I don't really even know what's going to happen tomorrow."

    hide iris normal
    show mc normal

    reader "Everyone's the same."

    hide mc normal
    show iris normal

    iris "Really? You seem like you have everything figured out."

    hide iris normal
    show mc normal

    reader "No way. I don't have a clue about what I'm doing either. I'm just 
    trying my best"

    hide mc normal
    show iris normal

    iris "I see..."

    narrator "She forces a weak smile before taking a step forward again."

    narrator "It doesn't take long to get to Iris' house first."

    iris "Goodbye, <Player Name>."

    narrator "Somehow, there was a hint of finality in her words."

    hide iris normal
    show mc normal

    reader "Goodbye."

    hide mc normal

label scene2:

    scene bg two

    narrator "The rest of the school year leading up to graduation and the 
    ensuing summer went by smoothly even though I found myself spending less 
    and less time with Iris, who was staying in town after graduation."
    
    narrator "We didn't really have anything to talk about the last few times we saw each 
    other. Still, I felt a twinge of disappointment when I didn't see her at 
    the train station right before I left."

# This ends the game.

return

