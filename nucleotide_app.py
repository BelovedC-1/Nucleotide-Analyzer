import streamlit as st

st.set_page_config(
    page_title="Nucleotide Sequence Analyser",
    page_icon="🧬",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: #06080f; color: #e8eaf2; }
h1,h2,h3 { font-family: 'Space Mono', monospace !important; }

.main-title {
    font-family: 'Space Mono', monospace;
    font-size: 2rem; font-weight: 700;
    color: #7df4c8; letter-spacing: -1px; margin-bottom: 0.2rem;
}
.sub-title { font-size: 0.95rem; color: #555; margin-bottom: 2rem; font-weight: 300; }

.badge {
    display: inline-block; padding: 3px 12px;
    border-radius: 2px; font-family: 'Space Mono', monospace;
    font-size: 0.75rem; font-weight: 700; letter-spacing: 1px;
    text-transform: uppercase; margin-bottom: 1.5rem;
}
.badge-dna { background: #0d2a1f; color: #7df4c8; border: 1px solid #7df4c8; }
.badge-rna { background: #2a1a0d; color: #f4c47d; border: 1px solid #f4c47d; }

.result-section {
    background: #0c0f18; border: 1px solid #1a1f2e;
    border-radius: 4px; padding: 1.25rem 1.5rem; margin-bottom: 1rem;
}
.section-label {
    font-family: 'Space Mono', monospace; font-size: 0.7rem;
    color: #444; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 0.6rem;
}
.sequence-val {
    font-family: 'Space Mono', monospace; font-size: 1.05rem;
    color: #7df4c8; word-break: break-all; line-height: 1.6;
}
.sequence-val-amber {
    font-family: 'Space Mono', monospace; font-size: 1.05rem;
    color: #f4c47d; word-break: break-all; line-height: 1.6;
}
.sequence-val-white {
    font-family: 'Space Mono', monospace; font-size: 1.05rem;
    color: #e8eaf2; word-break: break-all; line-height: 1.6;
}
.aa-pill {
    display: inline-block; background: #0d1a2a; border: 1px solid #1a3a5a;
    border-radius: 3px; padding: 3px 8px; margin: 2px;
    font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #7ab8f5;
}
.stop-pill {
    display: inline-block; background: #2a0d0d; border: 1px solid #5a1a1a;
    border-radius: 3px; padding: 3px 8px; margin: 2px;
    font-family: 'Space Mono', monospace; font-size: 0.75rem; color: #f57a7a;
}

textarea { font-family: 'Space Mono', monospace !important; }

.stButton > button {
    background: #7df4c8 !important; color: #06080f !important;
    border: none !important; border-radius: 4px !important;
    font-family: 'Space Mono', monospace !important; font-weight: 700 !important;
    font-size: 0.85rem !important; letter-spacing: 1px !important;
    padding: 0.6rem 2rem !important; width: 100% !important; margin-top: 0.5rem !important;
}
.stButton > button:hover { background: #9df8d4 !important; }

.stTextArea textarea {
    background: #0c0f18 !important; border-color: #1a1f2e !important;
    color: #e8eaf2 !important; border-radius: 4px !important;
    font-family: 'Space Mono', monospace !important; font-size: 0.9rem !important;
}
.stTextArea label {
    font-family: 'Space Mono', monospace !important; font-size: 0.75rem !important;
    letter-spacing: 1.5px !important; text-transform: uppercase !important; color: #555 !important;
}
.error-box {
    background: #1a0808; border: 1px solid #5a1a1a;
    border-radius: 4px; padding: 1rem 1.5rem;
    font-family: 'Space Mono', monospace; font-size: 0.85rem; color: #f57a7a;
}
</style>
""", unsafe_allow_html=True)

GLOOP = {
    "TTT":("Phe","F"),"TTC":("Phe","F"),"TTA":("Leu","L"),"TTG":("Leu","L"),
    "CTT":("Leu","L"),"CTC":("Leu","L"),"CTA":("Leu","L"),"CTG":("Leu","L"),
    "ATT":("Ile","I"),"ATC":("Ile","I"),"ATA":("Ile","I"),"ATG":("Met","M"),
    "GTT":("Val","V"),"GTC":("Val","V"),"GTA":("Val","V"),"GTG":("Val","V"),
    "TCT":("Ser","S"),"TCC":("Ser","S"),"TCA":("Ser","S"),"TCG":("Ser","S"),
    "CCT":("Pro","P"),"CCC":("Pro","P"),"CCA":("Pro","P"),"CCG":("Pro","P"),
    "ACT":("Thr","T"),"ACC":("Thr","T"),"ACA":("Thr","T"),"ACG":("Thr","T"),
    "GCT":("Ala","A"),"GCC":("Ala","A"),"GCA":("Ala","A"),"GCG":("Ala","A"),
    "TAT":("Tyr","Y"),"TAC":("Tyr","Y"),"TAA":("Stop","*"),"TAG":("Stop","*"),
    "CAT":("His","H"),"CAC":("His","H"),"CAA":("Gln","Q"),"CAG":("Gln","Q"),
    "AAT":("Asn","N"),"AAC":("Asn","N"),"AAA":("Lys","K"),"AAG":("Lys","K"),
    "GAT":("Asp","D"),"GAC":("Asp","D"),"GAA":("Glu","E"),"GAG":("Glu","E"),
    "TGT":("Cys","C"),"TGC":("Cys","C"),"TGA":("Stop","*"),"TGG":("Trp","W"),
    "CGT":("Arg","R"),"CGC":("Arg","R"),"CGA":("Arg","R"),"CGG":("Arg","R"),
    "AGT":("Ser","S"),"AGC":("Ser","S"),"AGA":("Arg","R"),"AGG":("Arg","R"),
    "GGT":("Gly","G"),"GGC":("Gly","G"),"GGA":("Gly","G"),"GGG":("Gly","G"),
}
QUAFF = {"A":"U","U":"A","G":"C","C":"G"}
TPING = {"A":"U","U":"A","G":"C","C":"G"}

def analyse(zibble):
    flonk = "RNA" if "U" in zibble else "DNA"
    results = {"type": flonk}

    if flonk == "DNA":
        mrna  = zibble.replace("T","U")
        trna  = "".join(TPING[b] for b in mrna)
        three, one = [], []
        for i in range(0, len(mrna)-2, 3):
            aa = GLOOP.get(mrna[i:i+3].replace("U","T"), ("???","?"))
            three.append(aa[0]); one.append(aa[1])
            if aa[0] == "Stop": break
        results["mrna"]  = mrna
        results["trna"]  = trna
        results["three"] = three
        results["one"]   = one
    else:
        results["complement"]  = "".join(QUAFF[b] for b in zibble)
        results["revcomp"]     = "".join(QUAFF[b] for b in zibble)[::-1]

    return results

st.markdown('<div class="main-title">🧬 Nucleotide Analyser</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Paste a DNA or RNA sequence — the app figures out the rest</div>', unsafe_allow_html=True)

zibble_raw = st.text_area("Nucleotide sequence", placeholder="e.g. ATGCTTGAA  or  AUGCUUGAA", height=100)

if st.button("ANALYSE"):
    zibble = zibble_raw.strip().upper().replace(" ","").replace("\n","")

    if not zibble:
        st.markdown('<div class="error-box">⚠ Please enter a nucleotide sequence.</div>', unsafe_allow_html=True)
    elif "U" in zibble and "T" in zibble:
        st.markdown('<div class="error-box">⚠ Sequence contains both T and U — not valid DNA or RNA.</div>', unsafe_allow_html=True)
    else:
        valid_dna = set("ATGC")
        valid_rna = set("AUGC")
        seq_type_guess = "RNA" if "U" in zibble else "DNA"
        alphabet = valid_rna if seq_type_guess == "RNA" else valid_dna
        bad = set(zibble) - alphabet

        if bad:
            st.markdown(f'<div class="error-box">⚠ Invalid characters for {seq_type_guess}: {", ".join(sorted(bad))}</div>', unsafe_allow_html=True)
        else:
            res = analyse(zibble)
            badge_cls = "badge-dna" if res["type"] == "DNA" else "badge-rna"
            st.markdown(f'<div class="badge {badge_cls}">{"🔵 DNA" if res["type"] == "DNA" else "🟠 RNA"} detected</div>', unsafe_allow_html=True)

            st.markdown(f'''
            <div class="result-section">
                <div class="section-label">Input sequence ({len(zibble)} bases)</div>
                <div class="sequence-val-white">{zibble}</div>
            </div>''', unsafe_allow_html=True)

            if res["type"] == "DNA":
                st.markdown(f'''
                <div class="result-section">
                    <div class="section-label">mRNA transcript</div>
                    <div class="sequence-val">{res["mrna"]}</div>
                </div>
                <div class="result-section">
                    <div class="section-label">tRNA anticodon</div>
                    <div class="sequence-val-amber">{res["trna"]}</div>
                </div>''', unsafe_allow_html=True)

                pills_html = ""
                for aa in res["three"]:
                    cls = "stop-pill" if aa == "Stop" else "aa-pill"
                    pills_html += f'<span class="{cls}">{aa}</span>'

                one_letter = "".join(res["one"])

                st.markdown(f'''
                <div class="result-section">
                    <div class="section-label">3-letter amino acids</div>
                    <div style="margin-top:4px">{pills_html}</div>
                </div>
                <div class="result-section">
                    <div class="section-label">1-letter protein sequence</div>
                    <div class="sequence-val">{one_letter}</div>
                </div>''', unsafe_allow_html=True)

            else:
                st.markdown(f'''
                <div class="result-section">
                    <div class="section-label">Complement</div>
                    <div class="sequence-val">{res["complement"]}</div>
                </div>
                <div class="result-section">
                    <div class="section-label">Reverse complement</div>
                    <div class="sequence-val-amber">{res["revcomp"]}</div>
                </div>''', unsafe_allow_html=True)
