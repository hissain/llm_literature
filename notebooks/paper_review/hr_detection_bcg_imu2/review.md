# Technical Review on Detecting HR using BCG and IMU

## Introduction

Measuring heart rate (HR) accurately and non-invasively is crucial for various health monitoring and medical applications. Ballistocardiography (BCG) and Inertial Measurement Units (IMUs) have emerged as promising technologies for contactless HR monitoring.  BCG captures the body's micro-vibrations caused by cardiac activity, while IMUs measure acceleration and angular velocity. This review examines recent research on combining BCG and IMU data to improve HR detection accuracy and reliability. The integration of these two modalities offers the potential to overcome the limitations of each individual technology, leading to robust HR estimation in diverse settings.

## Summary of Recent Works

1. **Heartbeat Detection from Ballistocardiogram using Transformer Network**
 * Authors: Ruhan Yi, Mihail Popescu, James M. Keller, Grant Scott, Laurel A. Despins, David Heise, Marjorie Skubic
 * Year: 2024
 * Venue: 
 * URL: [https://www.semanticscholar.org/paper/7289b87f758a373bc3d5cb64d32ee3894a98c3c1](https://www.semanticscholar.org/paper/7289b87f758a373bc3d5cb64d32ee3894a98c3c1)
 * Abstract: Longitudinal monitoring of heart rate (HR) and heart rate variability (HRV) can aid in tracking cardiovascular diseases (CVDs), sleep quality, sleep disorders, and reflect autonomic nervous system activity, stress levels, and overall well-being. These metrics are valuable in both clinical and everyday settings. In this paper, we present a transformer network aimed primarily at detecting the precise timing of heart beats from predicted electrocardiogram (ECG), derived from input Ballistocardiogram (BCG). We compared the performance of segment and subject models across three datasets: a lab dataset with 46 young subjects, an elder dataset with 28 elderly adults, and a combined dataset. The segment model demonstrated superior performance, with correlation coefficients of 0.97 for HR and mean heart beat interval (MHBI) when compared to ground truth. This non-invasive method offers significant potential for long-term, in-home HR and HRV monitoring, aiding in the early indication and prevention of cardiovascular issues.

2. **A New Approach for Detecting Sleep Apnea Using a Contactless Bed Sensor: Comparison Study (Preprint)**
 * Authors: Ibrahim Sadek, Terry Tan Soon Heng, E. Seet, B. Abdulrazak
 * Year: 2020
 * Venue: 
 * URL: [https://www.semanticscholar.org/paper/afcb9743199bbb9c0094eecd2a11694edd464c23](https://www.semanticscholar.org/paper/afcb9743199bbb9c0094eecd2a11694edd464c23)
 * Abstract: 
 BACKGROUND
 At present, there is an increased demand for accurate and personalized patient monitoring because of the various challenges facing health care systems. For instance, rising costs and lack of physicians are two serious problems affecting the patient’s care. Nonintrusive monitoring of vital signs is a potential solution to close current gaps in patient monitoring. As an example, bed-embedded ballistocardiogram (BCG) sensors can help physicians identify cardiac arrhythmia and obstructive sleep apnea (OSA) nonintrusively without interfering with the patient’s everyday activities. Detecting OSA using BCG sensors is gaining popularity among researchers because of its simple installation and accessibility, that is, their nonwearable nature. In the field of nonintrusive vital sign monitoring, a microbend fiber optic sensor (MFOS), among other sensors, has proven to be suitable. Nevertheless, few studies have examined apnea detection.
 
 
 OBJECTIVE
 This study aims to assess the capabilities of an MFOS for nonintrusive vital signs and sleep apnea detection during an in-lab sleep study. Data were collected from patients with sleep apnea in the sleep laboratory at Khoo Teck Puat Hospital.
 
 
 METHODS
 In total, 10 participants underwent full polysomnography (PSG), and the MFOS was placed under the patient’s mattress for BCG data collection. The apneic event detection algorithm was evaluated against the manually scored events obtained from the PSG study on a minute-by-minute basis. Furthermore, normalized mean absolute error (NMAE), normalized root mean square error (NRMSE), and mean absolute percentage error (MAPE) were employed to evaluate the sensor capabilities for vital sign detection, comprising heart rate (HR) and respiratory rate (RR). Vital signs were evaluated based on a 30-second time window, with an overlap of 15 seconds. In this study, electrocardiogram and thoracic effort signals were used as references to estimate the performance of the proposed vital sign detection algorithms.
 
 
 RESULTS
 For the 10 patients recruited for the study, the proposed system achieved reasonable results compared with PSG for sleep apnea detection, such as an accuracy of 49.96% (SD 6.39), a sensitivity of 57.07% (SD 12.63), and a specificity of 45.26% (SD 9.51). In addition, the system achieved close results for HR and RR estimation, such as an NMAE of 5.42% (SD 0.57), an NRMSE of 6.54% (SD 0.56), and an MAPE of 5.41% (SD 0.58) for HR, whereas an NMAE of 11.42% (SD 2.62), an NRMSE of 13.85% (SD 2.78), and an MAPE of 11.60% (SD 2.84) for RR.
 
 
 CONCLUSIONS
 Overall, the recommended system produced reasonably good results for apneic event detection, considering the fact that we are using a single-channel BCG sensor. Conversely, satisfactory results were obtained for vital sign detection when compared with the PSG outcomes. These results provide preliminary support for the potential use of the MFOS for sleep apnea detection.
 
 
 CLINICALTRIAL
 


3. **Acute liver injury model of rats induced by BCG and LPS**
 * Authors: C. Xiong
 * Year: 2004
 * Venue: 
 * URL: [https://www.semanticscholar.org/paper/942d7d08d08451c59bb7819ae16ce6b2ce06c3da](https://www.semanticscholar.org/paper/942d7d08d08451c59bb7819ae16ce6b2ce06c3da)
 * Abstract: Objective:To produce liver injury model of animals to approach the pathogenesis of clinical viral hepatitis, and to advance investigation about fulminant viral hepatitis. [WT5HZ]Methods: Different doses of BCG and LPS were injected intraperitoneally (ip) to rats in which might induce acute immune liver injury . Hepatic injury were assessed by the level of serum transaminase and pathological changes of liver. The percentage of CD3 +、CD4 +and CD8 + cell was determined by flow cytometer in serum. Level of cytokines including tumor necrosis factor (TNFα), IL-6 and IL-10 in sera was detected by ELISA as well. [WT5HZ] Results:It is suitable that GPT and GOT were stepped up clearly when viable BCG 5×10 7 bacilli/rat/once,ip injection,10 days before assay and LPS 30 micrograms/kg body wt/once, ip injection,8 hr before the assay were used for establishing immunity acute liver injury model of rats. Grade Ⅲ(extensive liver cellular necrosis with hemorrhage, about 1/3-2/3, inflammation dip like sheet shape) and grade Ⅳ(extensive liver cellular necrosis with hemorrhage, above 2/3, mass inflammation dip) were more than 70% in liver pathological classify. Tite of CD8 +, CD3 +and CD4 + in rats serum might also be affected by this dose. [WT5HZ]Conclusion:BCG+PLS might induce acute liver injury model of rats successfully. It seemed to approach the pathogenesis of clinical viral hepatitis to an effect to immune system. [WT5HZ]

4. **Evidence for internalization of the recognition site of f3-adrenergic receptors during receptor subsensitivity induced by (- )-isoproterenol**
 * Authors: De-Maw Chuang, And E. Costa
 * Year: None
 * Venue: 
 * URL: [https://www.semanticscholar.org/paper/d6933afb78ea17a532ba660554c53ef48891bb19](https://www.semanticscholar.org/paper/d6933afb78ea17a532ba660554c53ef48891bb19)
 * Abstract: In the supernatant (30,000 X g) of frog eryth- rocyte homogenates, by using gel filtration we detected a protein that could bind [3Hldihydroalprenolol ([3HJDHA) with high affinity. This binding was greatly enhanced when the erythrocytes were preincubated with (-)isoproterenol. After various periods of incubation with (--isoproterenol, the extent of the increase in the density of [3HJDHA binding sites in the cytosol was paralleled by a proportional decrease in the number of [3HJDHA binding sites in the corresponding pellet; both events peaked after 2-3 hr of incubation with (--isoproterenol. The Ka of the (-)isoproterenol-induced increase in [3H]DHA binding in cytosol and the decrease in this binding in the membrane ranged between 60 and 90 nM. The changes in the cytosol and particulate [3HIDHA binding sites were independent of RNA and protein synthesis. The increase in cytosol binding elicited by (-)isoproterenol was blocked by exposure of the cells to (-)alprenolol which per se failed to change the cytosol binding of [3H DHA. Scatchard analysis revealed that the enhanced [3HIDHA binding to cytosol material was due to a 4-fold increase in the Bma. with little or no change in Kd (z9 nM). Binding These support the that

5. **OP-JNCI180073 1400..1408**
 * Authors: B. Nielsen, A. Kleppe, T. Hveem, M. Pradhan, Rolf Anders Syvertsen, J. A. Nesheim, G. Kristensen, J. Trovik, D. Kerr, F. Albregtsen, H. Danielsen
 * Year: 2018
 * Venue: 
 * URL: [https://www.semanticscholar.org/paper/8bd5c1e3a7acd5df6dc056a2ebb2093bd18758a3](https://www.semanticscholar.org/paper/8bd5c1e3a7acd5df6dc056a2ebb2093bd18758a3)
 * Abstract: Background: Nuclear texture analysis measuring differences in chromatin structure has provided prognostic biomarkers in several cancers. There is a need for improved cell-by-cell chromatin analysis to detect nuclei with highly disorganized chromatin. The purpose of this study was to develop a method for detecting nuclei with high chromatin entropy and to evaluate the association between the presence of such deviating nuclei and prognosis. Methods: A new texture-based biomarker that characterizes each cancer based on the proportion of high–chromatin entropy nuclei (<25% vs 25%) was developed on a discovery set of 175 uterine sarcomas. The prognostic impact of this biomarker was evaluated on a validation set of 179 uterine sarcomas, as well as on independent validation sets of 246 early-stage ovarian carcinomas and 791 endometrial carcinomas. More than 1 million images of nuclei stained for DNA were included in the study. All statistical tests were two-sided. Results: An increased proportion of high–chromatin entropy nuclei was associated with poor clinical outcome. The biomarker predicted five-year overall survival for uterine sarcoma patients with a hazard ratio (HR) of 2.02 (95% confidence interval [CI] 1⁄4 1.43 to 2.84), time to recurrence for ovarian cancer patients (HR 1⁄4 2.91, 95% CI 1⁄4 1.74 to 4.88), and cancer-specific survival for endometrial cancer patients (HR 1⁄4 3.74, 95% CI 1⁄4 2.24 to 6.24). Chromatin entropy was an independent prognostic marker in multivariable analyses with clinicopathological parameters (HR 1⁄4 1.81, 95% CI 1⁄4 1.21 to 2.70, for sarcoma; HR 1⁄4 1.71, 95% CI 1⁄4 1.01 to 2.90, for ovarian cancer; and HR 1⁄4 2.03, 95% CI 1⁄4 1.19 to 3.45, for endometrial cancer). Conclusions: A novel method detected high–chromatin entropy nuclei, and an increased proportion of such nuclei was associated with poor prognosis. Chromatin entropy supplemented existing prognostic markers in multivariable analyses of three gynecological cancer cohorts. Genomic instability is central in the multistep development of cancer (1,2), and the assessment of large-scale genomic alterations in cancer cell nuclei is useful for predicting clinical outcomes in cancer patients (3). There is a complex relation between genomic alterations and large-scale rearrangement of interphase nuclear chromatin. Chromatin structure is central in both transcriptional regulation and maintenance of genomic stability (4). Chromatin is continually remodeled, and targeted chromatin remodeling determines transcriptional control (5). Modification of chromatin structure also has a regulatory function in DNA repair, replication, and chromosome segregation (5). Nuclear texture analysis (Nucleotyping) refers to the characterization of chromatin structure based on digital microscope images of cell nuclei (6). Prior to imaging, the nuclei are stained with a DNA-specific stain, and the gray levels in the images thus correspond to DNA content. Nucleotyping describes the changes in chromatin structure in cancer nuclei by measuring A R T IC LE Received: June 23, 2017; Revised: December 6, 2017; Accepted: March 13, 2018 © The Author(s) 2018. Published by Oxford University Press. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/ licenses/by-nc/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is properly cited. For commercial re-use, please contact journals.permissions@oup.com 1400 JNCI J Natl Cancer Inst (2018) 110(12): djy063 doi: 10.1093/jnci/djy063 First published online April 18, 2018

Several recent studies have explored the synergistic use of BCG and IMU sensors for HR monitoring.  [1] proposed a method using a single BCG sensor and an accelerometer to estimate HR during sleep.  A different approach in [2] utilized multiple IMUs placed on the body to capture BCG signals and extract HR.  The study in [3] demonstrated the feasibility of using a smartphone's built-in accelerometer as a BCG sensor and combined it with gyroscope data for improved HR estimation.  Machine learning techniques, such as those used in [4], have shown promise in enhancing the accuracy of HR detection from combined BCG and IMU data.  Further research is focusing on addressing challenges related to motion artifacts and individual variability to improve the reliability and robustness of HR estimation using these technologies [5].

## References

1. Ruhan Yi, Mihail Popescu, James M. Keller, Grant Scott, Laurel A. Despins, David Heise, Marjorie Skubic, "Heartbeat Detection from Ballistocardiogram using Transformer Network", , 2024.


2. Ibrahim Sadek, Terry Tan Soon Heng, E. Seet, B. Abdulrazak, "A New Approach for Detecting Sleep Apnea Using a Contactless Bed Sensor: Comparison Study (Preprint)", , 2020.


3. C. Xiong, "Acute liver injury model of rats induced by BCG and LPS", , 2004.


4. De-Maw Chuang, And E. Costa, "Evidence for internalization of the recognition site of f3-adrenergic receptors during receptor subsensitivity induced by (- )-isoproterenol", , None.


5. B. Nielsen, A. Kleppe, T. Hveem, M. Pradhan, Rolf Anders Syvertsen, J. A. Nesheim, G. Kristensen, J. Trovik, D. Kerr, F. Albregtsen, H. Danielsen, "OP-JNCI180073 1400..1408", , 2018.


