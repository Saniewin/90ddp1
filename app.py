import streamlit as st

# Set Streamlit Page Configuration - optimized for modern mobile viewports (e.g., Samsung Galaxy S26 Ultra)
st.set_page_config(
    page_title="Phase I Compliance Auditing App",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS to inject a premium "Samsung OneUI" visual aesthetic (curved corners, rich blues, readable mobile cards)
st.markdown("""
<style>
    /* Main body background & mobile canvas layout */
    .stApp {
        background-color: #F8F9FD;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Device frame mockup for Samsung S26 Ultra centered canvas */
    @media (min-width: 450px) {
        .block-container {
            max-width: 430px !important;
            padding: 20px !important;
            background: #FFFFFF;
            border-radius: 40px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
            margin-top: 10px;
            margin-bottom: 20px;
            border: 8px solid #202124;
        }
    }
    
    /* Sleek card styling for checklist containers */
    .audit-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
        border: 1px solid #ECEFF1;
    }
    
    /* Premium header styles */
    .app-title {
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #1A237E;
        text-align: center;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    
    .app-subtitle {
        font-size: 13px;
        color: #78909C;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .policy-tag {
        font-size: 11px;
        font-weight: 700;
        background-color: #E8EAF6;
        color: #283593;
        padding: 3px 8px;
        border-radius: 12px;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    /* Color-coded indicator labels */
    .status-compliant {
        font-size: 12px;
        font-weight: bold;
        color: #2E7D32;
        background-color: #E8F5E9;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
    }
    
    .status-noncompliant {
        font-size: 12px;
        font-weight: bold;
        color: #C62828;
        background-color: #FFEBEE;
        padding: 4px 10px;
        border-radius: 8px;
        display: inline-block;
    }
    
    /* Custom button styling */
    .stButton>button {
        background-color: #1E3A8A !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 700 !important;
        width: 100%;
        border: none !important;
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# Title & Metadata
st.markdown('<div class="app-title">CNS Psychological Services</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Phase I Mobile Audit Assistant • Samsung S26 Ultra Optimized</div>', unsafe_allow_html=True)

# Initialize Session State for interactive checklists to persist selections
if 'audit_data' not in st.session_state:
    st.session_state.audit_data = {
        # Objective 1: LARA Supervision Compliance
        "lara_logs_exist": {"compliant": True, "notes": "Form LARA/BPL Rev. 6/25 logs verified for LLPs"},
        "lara_4hours": {"compliant": True, "notes": "Minimum 4 hours/month face-to-face LP supervision confirmed"},
        "lara_signoff": {"compliant": True, "notes": "Official supervision evaluation logs signed and uploaded"},
        "lara_cosignature": {"compliant": True, "notes": "Fully Licensed LP co-signatures on clinical notes verified"},
        
        # Objective 2: BTPRC Safeguards (MDHHS APF 167)
        "btp_unanimous": {"compliant": True, "notes": "Unanimous committee approval obtained for restrictive plans"},
        "btp_composition": {"compliant": True, "notes": "Committee includes Licensed Psychologist/BCBA, MD/DO, and ORR rep"},
        "btp_medical": {"compliant": True, "notes": "MD/DO physical exam completed to rule out biological causes"},
        "btp_fba_attached": {"compliant": True, "notes": "FBA completed with baseline A-B-C behavioral data"},
        "btp_no_aversives": {"compliant": True, "notes": "Zero prohibited aversive or emergency physical codes used"},
        
        # Objective 3: Clinical Documentation & CPT Coding
        "cpt_feedback_96130": {"compliant": True, "notes": "Interactive feedback sessions documented for all 96130 claims"},
        "cpt_time_minimum": {"compliant": True, "notes": "CPT 96130 evaluations support 31+ minute threshold minimums"},
        "cpt_tech_segregation": {"compliant": True, "notes": "Technician scoring (96138) strictly segregated from provider (96136)"},
        "cpt_stratified_audit": {"compliant": True, "notes": "30-case stratified chart audit proportionally extracted"},
        
        # Objective 4: CCBHC Access & Triage Velocity
        "triage_prelim_screening": {"compliant": True, "notes": "Preliminary screening and risk assessment conducted at first contact"},
        "triage_michicans_locus": {"compliant": True, "notes": "Required tools (MichiCANS Screener/LOCUS) integrated in triage"},
        "triage_urgent_1day": {"compliant": True, "notes": "Urgent cases scheduled and initiated within 1 business day"},
        "triage_routine_14day": {"compliant": True, "notes": "Routine assessments initiated within 14 calendar days"},
        "triage_waitlist_interim": {"compliant": True, "notes": "Zero waitlists maintained; care coordination interim services active"}
    }

# Define Checklist Definitions linked with policies and remediation steps
checklist_defs = {
    "LARA Supervision Compliance": {
        "policy": "LARA Rule 338.2569 & MCL 333.18223 (Michigan Public Health Code)",
        "tasks": {
            "lara_logs_exist": {
                "label": "Official LARA logs exist for all active LLPs/TLLPs.",
                "remediation": "Immediately download the official Psychology Supervision Evaluation form (LARA/BPL, Rev. 6/25) for any staff member missing active logs and mandate immediate record recreation."
            },
            "lara_4hours": {
                "label": "Each LLP receives at least 4 hours per month of individual, face-to-face LP supervision.",
                "remediation": "Block designated 'LP-LLP Supervision' hours directly into LP calendars. If monthly limits are missed, retroactively suspend billing for those hours to prevent billing recoupment."
            },
            "lara_signoff": {
                "label": "Official supervision logs are signed by fully licensed LP and submitted.",
                "remediation": "Perform a retrospective administrative signature run. Require LPs and LLPs to complete and sign LARA logs prior to releasing the final monthly payroll."
            },
            "lara_cosignature": {
                "label": "LPs co-sign clinical notes prior to claim release.",
                "remediation": "Modify EHR routing rules to prevent any claim involving LLP-rendered psychometrics from being released to CHAMPS until the supervising LP co-signs."
            }
        }
    },
    "BTPRC Compliance (MDHHS APF 167)": {
        "policy": "MDHHS APF 167 Guidelines, Michigan Mental Health Code, & CCBHC Handbook 8.D.1.5",
        "tasks": {
            "btp_unanimous": {
                "label": "Unanimous committee approval obtained for restrictive BTPs.",
                "remediation": "Immediately suspend the use of the proposed restrictive interventions. Schedule an urgent BTPRC review session to secure unanimous approval."
            },
            "btp_composition": {
                "label": "Committee composition includes LP/BCBA, Physician, and Recipient Rights Representative.",
                "remediation": "If any key member is absent, reschedule the meeting. Non-CMHSP CCBHCs must route plans to the state-level MDHHS BTPRC through their assigned Certification Specialist."
            },
            "btp_medical": {
                "label": "MD/DO comprehensive physical examination completed to rule out biological causes of behavior.",
                "remediation": "Halt the plan. Schedule an immediate primary care physical exam for the consumer to rule out organic factors like undiagnosed dental pain, infections, or medication side effects."
            },
            "btp_fba_attached": {
                "label": "Structured FBA attached, documenting baseline Antecedent-Behavior-Consequence data.",
                "remediation": "Deploy a clinical supervisor to execute a rapid 5-day structured behavioral observation. Collect baseline A-B-C data and integrate it into a modified FBA format."
            },
            "btp_no_aversives": {
                "label": "Zero prohibited aversives or emergency management written as standard responses.",
                "remediation": "Immediately remove any reference to physical restraints or unpleasant stimuli from the BTP. Re-train staff on Positive Behavior Supports (PBS) and distress tolerance skills (DBT/ACT)."
            }
        }
    },
    "Clinical Documentation & CPT Coding": {
        "policy": "AMA CPT Manual, CMS National Correct Coding Initiative (NCCI) Edits, & CARF Standards",
        "tasks": {
            "cpt_feedback_96130": {
                "label": "CPT 96130 billing is backed by documented interactive feedback sessions with patient/caregiver.",
                "remediation": "If feedback is missing, self-disclose and adjust billing or arrange an immediate feedback session if clinically appropriate and within allowable timelines."
            },
            "cpt_time_minimum": {
                "label": "CPT 96130 evaluation time logged meets the 31-minute threshold minimum.",
                "remediation": "Halt the claim. Direct the provider to review clinical notes, accurately reconstruct clinical decision-making, and document the correct time spent prior to rebilling."
            },
            "cpt_tech_segregation": {
                "label": "Technician scoring (96138) strictly segregated from provider admin (96136).",
                "remediation": "Apply NCCI Modifier 59 or XE to same-day provider and technician encounters. Conduct CPT coding training for the revenue cycle management and billing teams."
            },
            "cpt_stratified_audit": {
                "label": "Randomized 30-case stratified chart audit (adult, pediatric, geriatric) proportionally completed.",
                "remediation": "Increase administrative hours for the Program Manager. Mandate the completion of the 30-chart review before Phase I expires on Day 30."
            }
        }
    },
    "CCBHC Access & Triage Velocity": {
        "policy": "SAMHSA 2023 CCBHC Criteria, MDHHS CCBHC Handbook 8.B.9, & CareConnect360 Integration",
        "tasks": {
            "triage_prelim_screening": {
                "label": "Preliminary screening and risk assessment conducted immediately at first contact.",
                "remediation": "Mandate that intake staff perform rapid preliminary screenings over the phone or in person, recording all risk parameters in the EHR."
            },
            "triage_michicans_locus": {
                "label": "Required State-designated level-of-care tools (MichiCANS Screener/LOCUS) integrated.",
                "remediation": "Coordinate with the training department. Ensure all intake clinicians are certified on MichiCANS (for youth) and LOCUS (for adults). Honor existing scores in CareConnect360."
            },
            "triage_urgent_1day": {
                "label": "Urgent assessments scheduled and initiated within 1 business day of contact.",
                "remediation": "Incorporate open access or same-day walk-in slots for high-acuity referrals. Leverage telehealth modules to bypass regional clinic wait times."
            },
            "triage_routine_14day": {
                "label": "Routine assessments initiated within 14 calendar days of contact.",
                "remediation": "Configure automated EHR system notifications that flag referrals approaching the 10-day mark to prompt rapid intake scheduling."
            },
            "triage_waitlist_interim": {
                "label": "Zero waitlists maintained; care coordination interim services active.",
                "remediation": "Deploy immediate interim care coordination services, peer recovery support, and brief screenings (CPT 96127) to engage the client while awaiting full testing."
            }
        }
    }
}

# Create Tabs for Navigation (Checklist, Findings Summary, Strengths Integration)
tab1, tab2, tab3 = st.tabs(["📋 Audit Deck", "📊 Live Summary", "🧠 Scott's Strengths"])

# ================= TAB 1: INTERACTIVE AUDIT CHECKLIST =================
with tab1:
    st.write("Perform real-time compliance audits. Mark tasks as 'Compliant' or 'Out of Compliance' to view remediation protocols.")
    
    for category_name, category_info in checklist_defs.items():
        st.markdown(f'<div class="policy-tag">{category_info["policy"]}</div>', unsafe_allow_html=True)
        st.markdown(f"#### **{category_name}**")
        
        for task_id, task_info in category_info["tasks"].items():
            # Retrieve persistent session state
            is_compliant_state = st.session_state.audit_data[task_id]["compliant"]
            
            # Use columns for checklist representation
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(task_info["label"])
            with col2:
                # Custom selection to mark compliance
                compliance_val = st.selectbox(
                    "Status",
                    ["Compliant", "Non-Compliant"],
                    index=0 if is_compliant_state else 1,
                    key=f"sel_{task_id}",
                    label_visibility="collapsed"
                )
                
            # Update session state based on selection
            is_compliant = (compliance_val == "Compliant")
            st.session_state.audit_data[task_id]["compliant"] = is_compliant
            
            # Context-specific Remediation Box (Renders only on Out of Compliance)
            if not is_compliant:
                st.markdown(
                    f'<div style="background-color:#FFF3CD; padding:12px; border-radius:12px; border-left: 5px solid #FFC107; margin-bottom:12px; font-size:12px;">'
                    f'⚠️ <strong>Out of Compliance Remediation Protocol:</strong><br>{task_info["remediation"]}'
                    f'</div>',
                    unsafe_allow_html=True
                )
        st.markdown("<hr style='margin: 8px 0 20px 0;'>", unsafe_allow_html=True)

# ================= TAB 2: EXACTIVE FINDINGS SUMMARY =================
with tab2:
    st.subheader("Phase I Audit Report Summary")
    
    # Calculate counts
    total_tasks = len(st.session_state.audit_data)
    compliant_tasks = sum(1 for k, v in st.session_state.audit_data.items() if v["compliant"])
    non_compliant_tasks = total_tasks - compliant_tasks
    compliance_percentage = (compliant_tasks / total_tasks) * 100
    
    # Render modern card statistics
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.metric("Compliant Tasks", f"{compliant_tasks}/{total_tasks}", f"{compliance_percentage:.1f}%")
    with col_stat2:
        st.metric("Out of Compliance", f"{non_compliant_tasks}", delta_color="inverse")
        
    # Visual progress bar
    st.progress(compliant_tasks / total_tasks)
    
    st.markdown("### **Verified Findings & Correct Items**")
    compliant_found = False
    for category_name, category_info in checklist_defs.items():
        comp_items = []
        for task_id, task_info in category_info["tasks"].items():
            if st.session_state.audit_data[task_id]["compliant"]:
                comp_items.append(task_info["label"])
        
        if comp_items:
            compliant_found = True
            st.markdown(f"🔹 **{category_name}**")
            for item in comp_items:
                st.markdown(f"✓ *{item}*")
                
    if not compliant_found:
        st.write("No compliant tasks identified. Overhaul required immediately.")

    st.markdown("### **Vulnerabilities & Non-Compliant Items**")
    non_compliant_found = False
    for category_name, category_info in checklist_defs.items():
        non_comp_items = []
        for task_id, task_info in category_info["tasks"].items():
            if not st.session_state.audit_data[task_id]["compliant"]:
                non_comp_items.append((task_info["label"], task_info["remediation"]))
        
        if non_comp_items:
            non_compliant_found = True
            st.markdown(f"❌ **{category_name}**")
            for item, rem in non_comp_items:
                st.markdown(f"🚨 **Issue:** {item}")
                st.markdown(
                    f'<div style="background-color:#FFEBEE; padding:10px; border-radius:10px; border-left: 4px solid #D32F2F; margin-bottom:8px; font-size:12px;">'
                    f'🛠️ <strong>Action Plan:</strong> {rem}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                
    if not non_compliant_found:
        st.success("🎉 Spectacular! All Phase I operational tasks are 100% compliant with state, federal, and CARF guidelines.")

# ================= TAB 3: CLIFTONSTRENGTHS BLUEPRINT =================
with tab3:
    st.subheader("Scott's Top 5 Strengths Blueprint")
    st.write("See how Dr. Scott Niewinski can strategically deploy his dominant CliftonStrengths to drive Phase I implementation:")
    
    strengths_map = {
        "🧠 Learner": {
            "focus": "Meticulous knowledge discovery and process audits",
            "application": "Drives the 30-case stratified chart audit and LARA log review by treating compliance mapping as an active intellectual journey from discovery to full clinical mastery."
        },
        "🎯 Strategic": {
            "focus": "Billing modifier patterns and workflow triage algorithms",
            "application": "Quickly identifies systemic revenue leakage patterns within historical CPT denials and establishes immediate billing modifiers XE/59 guidelines."
        },
        "🤝 Individualization": {
            "focus": "Tailored supervision and custom clinical feedback",
            "application": "Recognizes the unique writing styles and developmental stages of junior LLPs during the chart audit, structuring supportive training plans rather than standardized reprimands."
        },
        "💡 Ideation": {
            "focus": "Designing Stepped-Care screening triage frameworks",
            "application": "Conceives out-of-the-box administrative solutions to eliminate waitlists, such as deploying brief CPT 96127 screenings at intake as an immediate bottleneck filter."
        },
        "🔍 Intellection": {
            "focus": "Deep root-cause analyses of compliance bottlenecks",
            "application": "Introspectively ponders systemic bottlenecks within LPC/LP/LLP supervision ratios, designing long-term centralized tracking portals rather than superficial paper workarounds."
        }
    }
    
    for s_name, s_info in strengths_map.items():
        with st.expander(s_name):
            st.markdown(f"**Operational Focus:** *{s_info['focus']}*")
            st.write(f"**Phase I Application:** {s_info['application']}")

# Disclaimer Footer
st.markdown("<hr style='margin-top: 30px;'>", unsafe_allow_html=True)
st.markdown(
    '<div style="font-size:10px; color:#90A4AE; text-align:center; padding-bottom:20px;">'
    'CNS Healthcare psychological services compliance platform is configured in strict accordance with '
    'Michigan LARA (MCL 333.18223), MDHHS APF 167, and SAMHSA CCBHC parameters.</div>',
    unsafe_allow_html=True
)
