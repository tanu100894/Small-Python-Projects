from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell( w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)

    # y = 10
    # # Set the lines
    # while True:
    #     y = y + 10
    #     if y < 295:
    #         pdf.line(10, y, 200, y)
    #     else:
    #         break
    for y in range(20,295,10):
        pdf.line(10, y, 200, y)


    # Set the footer
    pdf.ln(265)  # 'A4' page height is 298 mm
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # y = 0
        # # Set the lines
        # while True:
        #     y = y + 10
        #     if y < 295:
        #         pdf.line(10, y, 200, y)
        #     else:
        #         break
        for y in range(10, 295, 10):
            pdf.line(10, y, 200, y)

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")