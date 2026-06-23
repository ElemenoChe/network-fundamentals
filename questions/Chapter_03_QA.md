# Chapter 3 – Review Questions & Answers

## Q1 Describe how data is transferred across a fiber-optic cable.
**A:** Data is transferred by converting electrical signals into pulses of light. These light pulses travel through a transparent glass or plastic fiber core via total internal reflection. At the receiving end, a photodetector converts the light pulses back into electrical signals.

## Q2 List advantages of fiber-optic cable over copper-core cable.
**A:**
- **Higher Bandwidth:** Can carry much more data at higher speeds.
- **Longer Distances:** Signals can travel much further without needing regeneration.
- **Immunity to EMI/RFI:** Not affected by electromagnetic or radio frequency interference.
- **Security:** More difficult to tap into without detection.
- **Smaller Diameter and Lighter Weight:** Easier to install and takes up less space.
- **No Spark Hazard:** Does not carry electrical current, eliminating fire hazards in certain environments.

## Q3 Light is measured by its _____.
**A:** Wavelength.

## Q4 What is the wavelength range of visible light?
**A:** Approximately 380 nanometers to 750 nanometers.

## Q5 What are the three common wavelengths associated with fiber-optic cable?
**A:** 850 nm, 1300 nm (or 1310 nm), and 1550 nm.

## Q6 What is dispersion?
**A:** Dispersion is the spreading of a light pulse as it travels through a fiber-optic cable, causing the pulse to broaden. This broadening can lead to signal degradation and limits the bandwidth and distance capabilities, as broadened pulses can overlap and become indistinguishable.

## Q7 Name three physical factors that contribute to extrinsic losses.
**A:**
- **Microbends:** Small, localized deviations or imperfections in the fiber's geometry.
- **Macrobends:** Larger bends or curves in the fiber that exceed the minimum bend radius.
- **Poor splices or connectors:** Improperly made or damaged connections leading to misalignment, air gaps, or surface contamination.

## Q8 Describe Fresnel reflection loss.
**A:** Fresnel reflection loss occurs at the interface between two materials with different refractive indices, such as where light passes from the fiber core into an air gap and back into another fiber core. A portion of the light is reflected back toward the source rather than being transmitted, causing signal loss. This commonly occurs at fiber-optic connectors and splices if surfaces are not perfectly aligned or clean.

## Q9 What are the two classifications of fiber-optic cable based on the diameter of the core?
**A:** Multimode fiber (MMF) and single-mode fiber (SMF).

## Q10 How does the diameter of the fiber-optic cable core affect the distance light can travel?
**A:** Single-mode fiber (SMF), with its very small core diameter, allows light to travel along a single path, minimizing modal dispersion and enabling light to travel much longer distances. Multimode fiber (MMF), with its larger core diameter, allows multiple light paths, causing modal dispersion that limits the distance light can travel before pulses spread too much and become indistinguishable.

## Q11 Fiber-optic cable core diameter is expressed in _____.
**A:** Micrometers.

## Q12 What are the two most common sizes of multimode fiber-optic cable?
**A:** 50/125 µm and 62.5/125 µm. (The first number is the core diameter, the second is the cladding diameter.)

## Q13 What is the IEEE 802 standard for Gigabit Ethernet?
**A:** IEEE 802.3z (for fiber and coaxial cable) and IEEE 802.3ab (for copper twisted pair).

## Q14 What is the IEEE 802 standard for 10 Gigabit Ethernet?
**A:** IEEE 802.3ae (for fiber) and IEEE 802.3an (for 10GBASE-T over copper twisted pair).

## Q15 What do the following 10 Gigabit Ethernet acronyms represent: SW, LW, and EW?
**A:**
- **SW:** Short Wavelength (typically using 850 nm over multimode fiber)
- **LW:** Long Wavelength (typically using 1310 nm over single-mode fiber)
- **EW:** Extended Wavelength (typically using 1550 nm over single-mode fiber for longer distances)

## Q16 What is the range of FDDI?
**A:** The maximum range of FDDI (Fiber Distributed Data Interface) is 2 kilometers between stations, with a total fiber path of up to 100 km.

## Q17 Why does FDDI use two rings of cable?
**A:** FDDI uses two rings (a primary and a secondary ring) for redundancy and fault tolerance. If the primary ring fails or is cut, traffic can automatically switch to the secondary ring, ensuring network availability and resilience.

## Q18 List the five most common types of fiber-optic cable connectors.
**A:**
- SC (Subscriber Connector or Standard Connector)
- LC (Lucent Connector or Little Connector)
- ST (Straight Tip)
- FC (Ferrule Connector)
- MPO/MTP (Multi-fiber Push On/Multi-fiber Termination Push-on)

## Q19 What are some common causes of attenuation associated with fiber-optic cable splices?
**A:**
- **Misalignment:** Cores not perfectly centered.
- **Air gap:** A small space between the two fiber ends.
- **Contamination:** Dust, dirt, or oil on the fiber end faces.
- **Improper cleave angle:** The fiber ends are not cut perfectly perpendicular.
- **Fiber mismatch:** Connecting fibers with different core diameters or numerical apertures.
- **Excessive pressure or tension:** Damage during splicing.

## Q20 Using heat to join two fiber-optic cores is called a(n) _____ splice.
**A:** Fusion splice.

## Q21 What is required to test a short run of fiber-optic cable?
**A:** A light source and a power meter (LSPM) are typically required. This setup measures the optical loss (attenuation) of the cable segment.

## Q22 What device is commonly used to test long runs of fiber-optic cable?
**A:** An Optical Time-Domain Reflectometer (OTDR).

## Q23 What principle of fiber-optic cable loss does the OTDR use for measurements?
**A:** The OTDR uses the principle of backscattering (Rayleigh scattering) and Fresnel reflection. It sends a pulse of light and measures the light reflected back to determine distance and loss characteristics along the fiber.
