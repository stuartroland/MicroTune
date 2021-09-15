from Frequencies.Hz import Hz
from Intervals.Scalar import Scalar
from Intervals.Ratio import Ratio

a440 = Hz(440)
print(a440, "+", Ratio(1, 2), '+', Scalar(1.5), '=', a440 + Ratio(1, 2) + Scalar(1.5), '\n')

