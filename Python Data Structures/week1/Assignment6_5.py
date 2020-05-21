text = "X-DSPAM-Confidence:    0.8475";
rfg = text.find('0.8475')
low = text[rfg:]
print(float(low))
