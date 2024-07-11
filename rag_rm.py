from dspy.retrieve.faiss_rm import FaissRM

labels = ["pulmonary edema", "consolidation", "pleural effusion", "pneumothorax", "cardiomegaly"]

reports = [
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Chest pain. Comparison: Chest radiograph from XXXX, XXXX. Findings: The cardiac silhouette is borderline enlarged. Otherwise, there is no focal opacity. Mediastinal contours are within normal limits. There is no large pleural effusion. No pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Borderline enlargement of the cardiac silhouette without acute pulmonary disease. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Shortness of breath. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is evidence of bilateral pulmonary edema. The cardiac silhouette is normal. No pleural effusion or pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Bilateral pulmonary edema. No evidence of pleural effusion or pneumothorax. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Cough and fever. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is consolidation in the right lower lobe. The cardiac silhouette is normal. No pleural effusion or pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Right lower lobe consolidation. No pleural effusion or pneumothorax. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Chest pain. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is a small left pleural effusion. The cardiac silhouette is normal. No pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Small left pleural effusion. No pneumothorax. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Trauma. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is a right-sided pneumothorax. The cardiac silhouette is normal. No pleural effusion. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Right-sided pneumothorax. No pleural effusion. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Shortness of breath and leg swelling. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is moderate pulmonary edema and bilateral pleural effusion. The cardiac silhouette is enlarged. No pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Moderate pulmonary edema and bilateral pleural effusion. Cardiomegaly. No pneumothorax. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Fever and cough. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is a consolidation in the left upper lobe. The cardiac silhouette is normal. No pleural effusion or pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Left upper lobe consolidation. No pleural effusion or pneumothorax. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Routine check-up. Comparison: Chest radiograph from XXXX, XXXX. Findings: The cardiac silhouette is normal. No focal opacity. Mediastinal contours are within normal limits. There is no pleural effusion or pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Normal chest radiograph. No abnormalities detected. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Dyspnea. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is mild cardiomegaly. Bilateral pleural effusions are present. No evidence of pneumothorax. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Mild cardiomegaly with bilateral pleural effusions. No pneumothorax. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """,
    """
    RADIOLOGY REPORT

    Exam
    PA and lateral chest radiograph (2 views) (2 images) Date: XXXX, XXXX at XXXX hours Indication: Trauma. Comparison: Chest radiograph from XXXX, XXXX. Findings: There is a left-sided pneumothorax. The cardiac silhouette is normal. No pleural effusion. Transcribed by - PSCB Transcription Date - XXXX

    IMPRESSION
    Left-sided pneumothorax. No pleural effusion. DICTATED BY : Dr. XXXX XXXX XXXX XXXX XXXX ELECTRONICALLY SIGNED XXXX. XXXX XXXX XXXX XXXX XXXX TRANSCRIBED XXXX 11 XXXX XXXX  RADRES XXXX

    SIGNATURE
    XXXX
    """
]

# Ground Truth Labels for each report
ground_truth = [
    ["cardiomegaly"],
    ["pulmonary edema"],
    ["consolidation"],
    ["pleural_effusion"],
    ["pneumothorax"],
    ["pulmonary edema", "pleural effusion", "cardiomegaly"],
    ["consolidation"],
    [],
    ["cardiomegaly", "pleural effusion"],
    ["pneumothorax"]
]

document_chunks = reports

# Initialize the FaissRM class
rm = FaissRM(document_chunks=document_chunks)

print(rm(["Provide your question here"]))