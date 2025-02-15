# Manual Test Playthrough Instructions
This document outlines a manual test playthrough for the Deepwater Catch game.  
Follow the steps below to verify that the game behaves as expected.

---
## General Instructions
- Ideally, a manual test should be completed with every commit (or for major changes). It is up to the developer discretion when to conduct a manual test.
- Fill in the results for each step as you progress.
- After completion of a test, save the form under the name: `Manual-Test_MM-DD-YYYY.md` in this folder and commit.
- For each result, record PASS or FAIL, then give feedback in the notes section explaining what happened
- If a test is not able to be completed, that shall default to a FAIL and explanation of what happened shall be documented.
---
## Test Steps
### 1. Game Start  
- **Action:**  
  - Launch the game.  
  - Confirm that the main game screen is visible.

- **Expected Result:**  
  - The main game screen is displayed without errors.

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:***

---
### 2. Boat Movement  
- **Action:**  
  - Use the left and right arrow keys to move the boat.  
  - Ensure the boat moves horizontally and stays within the screen bounds.

- **Expected Result:**  
  - The boat moves left and right and does not go offscreen.

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:***

---
### 3. Fish Movement  
- **Action:**  
  - Observe the fish movement during gameplay.

- **Expected Result:**  
  - Fish move left and right at different speeds.

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:***

---
### 4. Hook Behavior (Automatic Return)  
- **Action:**  
  - Drop the hook and wait for it to touch the bottom.

- **Expected Result:**  
  - After touching the bottom, the hook automatically returns to its starting position.

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:***

---
### 5. Boat Disabled During Hook Drop  
- **Action:**  
  - While the hook is dropping, attempt to move the boat with the arrow keys.

- **Expected Result:**  
  - The boat should remain stationary until the hook returns.

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:***  

---
### 6. Partial Hook Reel Test  
- **Action:**  
  - Drop the hook and, midway through its descent, press space to trigger reeling in.

- **Expected Result:**  
  - The hook immediately starts moving upward as soon as space is pressed.

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:***

---
### 7. Catching Fish Logic  
- **Action:**  
  - Drop the hook and try to catch a fish.

- **Expected Result:**  
  - When the hook makes contact with a fish, it should attach to the hook and the hook should reel back up. 
  - The fish should stay attached to the hook and despawn after the hook is reeled. 
  - After catching a fish, look at the score keeper to ensure it did increment by 1.
  - Conduct a few more tests to ensure the catching mechanic works and score is kept properly

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:***

---
### 7. General Play Through 
- **Action:**  
  - Continue to play for a minimum of 1 minute.
  - Move the boat, drop the hook, try to catch fish
  - Stop intermittently to review fish movements and scoring etc.

- **Expected Result:**  
  - No other unexpected bugs or conditions not allowed in previous tests shall be observed

***Result:***  
 - [x] Pass
 - [ ] Fail

***Issues/Notes:*** (Report any unexpected behavior)

---
## Additional Information
- **Tester:**  M. Villa
- **Date of test:**  2/14/2025 :cupid:
- **Game Version Tested:** 0.2.1 Incoming
---

## Follow On Actions
List any action items if done as a a result of this test