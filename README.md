# QBI-Observer Lite+

**Software module for Cognitive and Metacognitive Self-Observation**  
Part of the scientific project **QBI-Core – Quantum Brain Interface**

## Module Description

**QBI-Observer Lite+** is a non-autonomous, simplified version of the metacognitive self-observation module within the broader architecture known as **QBI-Core (Quantum Brain Interface)**.

This module analyzes sequences of textual thoughts, with the goal of detecting and classifying:

- **Cognitive repetitions (mental loops)**  
- **Internal questions (explicit or implicit)**  
- **Emotionally relevant words** (e.g., fear, hope, curiosity, frustration)  
- **Metacognitive activity level** (classified as low, medium, or high)


## Technical Features

The module is implemented in Python 3.x and built using simple rule-based text analysis methods. It is lightweight, transparent, and easy to integrate into scientific testing environments.

**Core functions:**

- `aggiungi_pensiero(thought: str)`: adds a thought to the current session  
- `rileva_loop()`: returns any thoughts repeated more than once  
- `rileva_domande()`: detects thoughts formulated as questions  
- `riconosci_emozioni()`: identifies emotionally connoted words  
- `classificazione_metacognitiva()`: returns the metacognitive activity level (low, medium, high)  
- `get_diario_sessione()`: returns the full session thought log



## Limitations and Clarifications

This **Lite+ version** is a foundational module intended **exclusively for**:

- Scientific and academic testing  
- Experimental studies on metacognition  
- Transparent demonstrations of cognitive and metacognitive logic  
- Not suitable for commercial use or integration into autonomous decision-making systems

**Important:** This is **not** the complete version of QBI-Core.  
This module does **not** possess any form of artificial consciousness, persistent memory, or autonomous intentionality.


## QBI-Core and the AIC Paradigm

QBI-Core introduces a new category of artificial intelligence known as **Artificial Integrated Cognition (AIC)**.  
AIC aims to go beyond traditional AI by simulating advanced forms of self-observation, metacognition, and complex internal logic inspired by theories of quantum coherence in neuronal microtubules.

**QBI-Observer Lite+** serves as a minimal, controlled and open-source demonstration intended for the scientific community to promote transparency, ethical research and responsible development in this emerging domain.


## License and Ethical Usage

This module is released under the **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** license, with explicit additional restrictions:

- Non-commercial use only  
- Prohibited in autonomous systems, AGI, military, surveillance, or any context in violation of the **EU AI Act 2024**  
- Attribution to the original author is required (see Contact section)

See the included `LICENSE.txt` file for full legal terms.


## How to Use the Module

Here is a quick usage example to start testing the module:

```python
from observer import QBIObserverLite

observer = QBIObserverLite()

observer.aggiungi_pensiero('I don’t understand why I keep making the same mistake.')
observer.aggiungi_pensiero('Maybe I’m afraid of failing.')
observer.aggiungi_pensiero('I need to find a different approach.')
observer.aggiungi_pensiero('I don’t understand why I keep making the same mistake.')

print('Detected loops:', observer.rileva_loop())
print('Internal questions:', observer.rileva_domande())
print('Detected emotions:', observer.riconosci_emozioni())
print('Metacognitive classification:', observer.classificazione_metacognitiva())


Advanced Version
A more advanced, protected version of the QBI-Observer module exists, including integrated memory systems, learning capabilities, semantic graph generation, and deeper self-reflective processes.

To access the advanced version, request scientific collaboration, or receive more technical details, please contact the author directly.

Author Contact
Giuseppe Marino
Email: qbicore@pec.it
Phone: (+39) 348 5550525
