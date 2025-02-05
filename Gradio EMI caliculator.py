
import gradio as gr

def emi(principal, rate, tenure):
    rate = rate / (12 * 100)  # Convert annual interest rate to monthly and percentage to decimal
    emi = (principal * rate * (1 + rate) ** tenure) / ((1 + rate) ** tenure - 1)
    return round(emi, 2)


demo = gr.Interface(
  fn=emi,
  inputs=[
  
    gr.Number(label="Loan Amount"),
    gr.Number(label="Rate of interest"),
    gr.Number(label="Loan Tenure (Months)"),
    
  ],
  outputs=gr.Number(label="EMI (Monthly Installment)"),
  title="EMI Calculator",
  description="Enter the loan amount, annual interest rate, and tenure to calculate your EMI."
)  
demo.launch()