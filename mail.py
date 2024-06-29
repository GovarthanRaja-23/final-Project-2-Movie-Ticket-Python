import smtplib
def mail():
    try:                       
        your_mail=input("PLEASE ...Enter your Mail I'D SIR/MAM to recieve Movie Ticket bill to your Mail : ")
        op=smtplib.SMTP("smtp.gmail.com",587)
        op.starttls()

        #please enter Mail I'D and app password to run this code
        op.login("","")

        bill_file=open("bill.txt","r")
        bill_content = bill_file.read()
        subject = "Your Booking Summary for Movie Ticket"
        body = f"Subject: {subject}\n\n{bill_content}\n\nTHANKS FOR BOOKING TICKET"

        #Enter the mail I'D you provided above to run this code
        op.sendmail("",your_mail,body)

        op.quit()
        print("------>MAIL IS SENT TO THE CUSTOMER<------")
    except Exception as e:
        print("MAIL IS NOT SENT TO THE CUSTOMER DUE TO WRONG MAIL I'D (OR) SOME ERRORS")
