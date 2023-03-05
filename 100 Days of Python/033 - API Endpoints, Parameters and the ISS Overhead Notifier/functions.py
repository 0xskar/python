import smtplib
import email.message


def is_close(your_coordinates, iss_coordinates):
    print(f"Your x,y: {your_coordinates}, Iss x,y: {iss_coordinates}")
    # Define acceptable range
    higher_x, lower_x = your_coordinates[0] + 5, your_coordinates[0] - 5
    x_range = (lower_x, higher_x)
    higher_y, lower_y = your_coordinates[1] + 5, your_coordinates[1] - 5
    y_range = (lower_y, higher_y)
    print(f"X Range: {x_range}\nY Range: {y_range}")
    if x_range[0] < iss_coordinates[0] < x_range[1] and y_range[0] < iss_coordinates[1] < y_range[1]:
        return True
    else:
        return False


def sendmail(distance, send_to_email, password):
    m = email.message.Message()
    m['From'] = send_to_email
    m['To'] = send_to_email
    m['Subject'] = f"ISS is close! It's {distance}!"
    m.set_payload("The ISS is probably passing overhead right now, check it out!\nFrom Errol")

    connection = smtplib.SMTP("smtp.sendgrid.net", 587)
    connection.starttls()
    connection.login(user=send_to_email, password=password)
    connection.sendmail(to_addrs=m['To'], from_addr=m['From'], msg=m.as_string())
    connection.close()
