import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def greeting():
    return """t.me/xulbv\n\nCheck out this method crafted by the user above! They've shared a way for us to get a free VPS, completely for free.\n\n\n\nThe BMW X5 is a mid-size luxury crossover SUV produced by BMW.[1] The X5 made its debut in 1999 as the E53 model. It was BMW's first SUV. At launch, it featured all-wheel drive and was available with either a manual or automatic gearbox. The second generation was launched in 2006, and was known internally as the E70. The E70 featured the torque-split capable xDrive all-wheel drive system mated to an automatic gearbox. In 2009, the X5 M performance variant was released as a 2010 model.[2]

BMW marketed the X5 officially as a "Sports Activity Vehicle" (SAV),[3] rather than an SUV, to indicate its on-road handling capability despite its large dimensions.[4] The X5 signaled a shift away from the utilisation of body-on-frame construction, in favour of more modern monocoque chassis construction. Although the Mercedes-Benz M-Class was introduced more than a year prior to the X5, the X5 was the first to utilise a monocoque chassis. The M-Class used body-on-frame construction until its second generation.[5][6]

The X5 is primarily manufactured in North America, at BMW Group Plant Spartanburg. Assembly operations also took place in Russia by Avtotor until February 2022, along with operations in India, Indonesia, Malaysia, and Thailand. The X5 is also modified for armoured security versions, at the BMW de México Toluca plant.[7]

The automaker's SAV series, which was started by the X5, has expanded with derivations of other number-series BMWs. This began in 2003 with the X3, and continued in 2008 with the X6 (which shares its platform with the X5)."""

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
