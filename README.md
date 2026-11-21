# 📊 Unemployment in India - Covid Impact Analysis

India me Covid-19 Lockdown ke time Unemployment kitna bada, aur uske baad recovery kaisi hui - iska full analysis.

### 📂 Dataset
Maine 2 files ko merge karke use kiya hai, taaki pura timeline mile:
- `Unemployment_in_India.csv` - May 2019 to June 2020
- `Unemployment_Rate_upto_11_2020.csv` - Jan 2020 to Oct 2020

**Combined Timeline: May 2019 - Oct 2020**

Dono files CMIE se hai. Jan-June 2020 dono me common tha, isliye duplicates hata diye.

### 🛠️ Tech Stack
- Python, Pandas, Numpy
- Matplotlib, Seaborn

### ✨ Kya Kiya Maine?
1.  **Data Cleaning:** Column names clean kiye, `Region.1` duplicate column hataya, Date format fix kiya.
2.  **Data Merging:** Dono files ko `concat` karke ek banaya, duplicates remove kiye.
3.  **EDA & Visualization:** 6 Graphs banaye.

### 📈 6 Graphs
1.  **Full Trend:** May 2019 - Oct 2020 - Covid Spike + Recovery
2.  **Rural vs Urban:** Lockdown me Urban ko zyada maar padi
3.  **Worst vs Best States:** Kaunse state me sabse zyada / kam berozgari
4.  **Pre vs Lockdown vs Recovery:** 3 period ka comparison
5.  **Labour Participation:** Covid me logon ne kaam dhundna hi chhod diya
6.  **Correlation Heatmap:** Unemployment, Employed, Labour Participation ka relation

### 📊 Key Findings
- **Pre-Covid (Feb 2020 tak):** Unemployment ~ 7-8% tha
- **Lockdown (April 2020):** Unemployment ~ 23-24% tak pahunch gaya - 3x badh gaya
- **Recovery (Oct 2020 tak):** Phir se ~ 7-8% pe wapas aa gaya
- **Urban > Rural:** Urban me berozgari Rural se zyada badi

### ▶️ Kaise Chalaye?
```bash
pip install pandas numpy matplotlib seaborn
python unemployment_analysis.py
