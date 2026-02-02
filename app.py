# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from PIL import Image
import os

# ==================================================
# Page configuration
# ==================================================
st.set_page_config(
    page_title="Dr Xylia Q. Peters | Computational Researcher",
    layout="wide"
)

# ==================================================
# Helper function to safely load images
# ==================================================
def load_image(path, width=None):
    if os.path.exists(path):
        img = Image.open(path)
        st.image(img, width=width)
    else:
        st.info(f"Image not found: {path}")

# ==================================================
# Sidebar Navigation
# ==================================================
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "",
    (
        "Profile",
        "Research Interests",
        "Computational Expertise",
        "Research & Projects",
        "Publications",
        "Education & Training",
        "Contact"
    )
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Current Affiliation**")
st.sidebar.write(
    """
    Postdoctoral Fellow  
    Nano Drug Delivery Unit  
    University of KwaZulu-Natal
    """
)

# ==================================================
# Header Section
# ==================================================
col1, col2 = st.columns([1, 3])

with col1:
    load_image("profile.jpeg", width=180)

with col2:
    st.title("Dr Xylia Quintina Peters")
    st.subheader("Computational & Pharmaceutical Research Scientist")
    st.write(
        """
        Computational researcher specialising in **pharmaceutical chemistry,
        bioinformatics, and data analytics**, with a strong focus on applying
        **in silico modelling, molecular dynamics, and data-driven methods**
        to address complex biomedical challenges.
        """
    )

st.markdown("---")

# ==================================================
# PAGE CONTENT
# ==================================================
if page == "Profile":
    st.header("Researcher Profile")
    st.write(
        """
        I am a computational and pharmaceutical research scientist with extensive
        experience in **drug discovery, nanomedicine, and molecular modelling**.
        My research integrates **computational chemistry, bioinformatics, and
        applied data analytics** to investigate therapeutic targets in cancer,
        bacterial infections, and inflammatory diseases.

        I have authored multiple peer-reviewed publications, presented at national
        and international conferences, and actively contribute to interdisciplinary
        research environments bridging experimental and computational science.
        """
    )

elif page == "Research Interests":
    st.header("Research Interests & Methodological Focus")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Research Domains")
        st.markdown(
            """
            - Computational drug discovery  
            - Pharmaceutical nanotechnology  
            - Antimicrobial resistance & sepsis  
            - Cancer therapeutics  
            - Bioinformatics & systems biology  
            """
        )

    with col2:
        st.subheader("Methodological Focus")
        st.markdown(
            """
            - Molecular docking & molecular dynamics  
            - Structure-based drug design  
            - Pharmacophore modelling  
            - Statistical & exploratory data analysis  
            - Data-driven hypothesis generation  
            """
        )

elif page == "Computational Expertise":
    st.header("Computational & Technical Expertise")

    col1, col2 = st.columns(2)
    
    with col1:
              
    
        st.subheader("Computational Drug Design")
        st.markdown(
            """
            - Molecular docking & simulations  
            - Structure-based drug design  
            - Pharmacophore modelling  
            - AutoDock, PyRx, Chimera  
            """
        )

    with col2:
        
        st.subheader("Bioinformatics & Systems Biology")
        st.markdown(
            """
            - Sequence & structural analysis  
            - Pathway & target analysis  
            - Linux & HPC workflows  
            """
        )

    col3, col4 = st.columns(2)

    with col3:
        
        st.subheader("Data Analytics & Modelling")
        st.markdown(
            """
            - Python, Pandas, NumPy  
            - Exploratory data analysis  
            - Statistical modelling  
            """
        )

    with col4:
        
        st.subheader("Nanomedicine & Drug Delivery")
        st.markdown(
            """
            - Nanocarrier systems  
            - Drug delivery optimisation  
            - Translational pharmaceutical research  
            """
        )

    with st.expander("Detailed Technical Toolchain"):
        st.markdown(
            """
            **Modelling:** Maestro, Discovery Studio, AutoDock, PyRx  
            **Bioinformatics:** Ensembl, REST APIs, RStudio  
            **Data & Visualization:** Streamlit, Plotly, Matplotlib  
            **HPC & OS:** Linux, CHPC environments  
            """
        )

elif page == "Research & Projects":
    st.header("Core Research & Computational Projects")

   
    st.subheader("NLRP3 Inflammasome Inactivation (ACS Omega)")
    st.write(
    """
    **Objective:** Identify computational strategies for inflammasome inactivation  
    **Methods:** Docking, interaction profiling, molecular modelling  
    **Outcome:** Peer-reviewed publication with translational relevance
    """
)
    

    st.subheader("Tankyrase Inhibition in Cancer Therapy")
    st.write(
        """
        **Objective:** Elucidate molecular mechanisms of tankyrase inhibition  
        **Methods:** Molecular docking, molecular dynamics, structure-activity analysis  
        **Outcome:** Mechanistic insights supporting selective inhibitor development
        """
    )

    

elif page == "Publications":
    st.header("Recent Publications")

    st.markdown(
        """
        - **ACS Omega (2025):** Targeting the ADAM10-Alpha Hemolysin Axis Using Ascorbyl Stearate as a Potential Therapy in S. aureus Infections: In Silico and MST Studies.  
        - **Journal of Drug Delivery Science and Technology (2025):** Enhancing activity and overcoming ciprofloxacin resistance via multifunctional nanostructured lipid carriers.  
        - **International Journal of Pharmaceutics (2025):** Antimicrobial peptide-fucoidan nanoplexes: A novel multifunctional biomimetic nanocarrier for enhanced Vancomycin delivery against bacterial infections and sepsis.  
        - **Expert Opinion on Drug Delivery (2025):** Potential of nanocarrier-mediated delivery of vancomycin for MRSA infections.  
        - **ACS omega (2025):** Paving the Way for NLRP3 Inflammasome Inactivation Using ADAM10 and Alpha-Hemolysin: An In Silico Investigation.  

        *Full publication list available on request or via Google Scholar  https://scholar.google.com/citations?user=3TCHlJEAAAAJ&hl=en&oi=ao .*
        """
    )

elif page == "Education & Training":
    st.header("Education & Training")

    st.markdown(
        """
        
        2025-present: **Postgraduate Diploma – Data Analytics**  
        IIE Varsity College / Emeritus 
                
        2019-2023: **PhD – Pharmaceutical Chemistry**  
        University of KwaZulu-Natal  

        2017-2018: **MSc – Pharmaceutical Science**  
        University of KwaZulu-Natal  

        2012-2016: **BSc Honors– Medical Science Anatomy**  
        University of KwaZulu-Natal

        **Other Professional Training:**  
        Bioinformatics, HPC, Python, SQL, Molecular Modelling
        """
    )

elif page == "Contact":
    st.header("Contact & Academic Links")

    st.markdown(
        """
        📧 **Email:** xyliapeters@yahoo.com  
        💻 **GitHub:** https://github.com/xylomilo  
        🔗 **LinkedIn:** www.linkedin.com/in/xyliapeters-8a257aa3  
        📚 **Google Scholar:** https://scholar.google.com/citations?user=3TCHlJEAAAAJ&hl=en&oi=ao  
        """
    )

st.markdown("---")
st.caption("© Dr Xylia Q. Peters | Independent Research Profile")

