# PawPal+ Project Reflection

## 1. System Design

- The user should be able to add basic information about the pet and owner, such as name and age.
- The user should be able to edit or update any information about the pet or owner.
- The user should be able to generate a scuedule for their pets that allows the user to mark whether its been completed or not.

**a. Initial design**

- Briefly describe your initial UML design.

* My initial UML design models a simple pet care app that consist of 4 main classes, Pet, Owner, Task, and Schedular. 

- What classes did you include, and what responsibilities did you assign to each?

* Classes included:
- Pet: responsible for pet name, age, breed, and weight
- Owner: responsible for owner name, age, and pets
- Task: responsible for title, task time, and priority
- Schedular: responsible for keeping track of owner and listing task
 

**b. Design changes**

- Did your design change during implementation?

* Yes, I did. I noticed that keeping track of the owner age is not really important for a pet care app.

- If yes, describe at least one change and why you made it.

* Instead of keeping track of the owner age, I decided to keep track of the owner's email. I figured I could implement reminders on tasks.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

I went with time. I decided time was most important because it would be easier and more efficent like that. 

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
A tradeoff my scheduler makes is not being about to priorties tasks.
- Why is that tradeoff reasonable for this scenario?

In my opinion, I think the tradeoff of losing priorites task is reasonible as time more efficient. Also, I wanted to design it this way from the start. 
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?

I used AI for designing brainstorming, debugging, refactoring, and general questions. There were times where I was stuck and AI was always the to bale me out.

- What kinds of prompts or questions were most helpful?

I felt that the most helpful prompts were few shots. Giving the LLM examples on how I want it to be and do really helps me understand what it's doing. I feel like the driver.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.

There were times where the LLM wanted to change some of the files that wasn't on the intructions. So i had to decline majority of them.

- How did you evaluate or verify what the AI suggested?


I just reworded my prompt and told it not to change anything other than what I am telling it to do.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?

Some of the test I did included:
* if the task where truely being marked as complete
* if the amount of task being add where truely being added to the list

- Why were these tests important?

These are important because the whole point is to make an app that generates a schedule for users pets. If theses don't work than the app's main functions is useless, resulting in the app a failure.

**b. Confidence**

- How confident are you that your scheduler works correctly?
If I had to rate it from 1 to 5, I'd rate it as 4. I am sure it works fine but there are a lot of edge cases that aren't fixed yet. As long as the user uses it normally it should work fine.
- What edge cases would you test next if you had more time?

* If the pet doesn't exist
* If task are empty

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am just satisfied that the app works and runs for the most part.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the logic and redesign the whole thing. I felt like I gave the AI too much freedom. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that if you give the AI too much freedom, yes you will get it done, but you miss out on how you want it to be and look. 
