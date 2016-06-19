#!/usr/bin/env python

import re

class Egn:

  GENDER_MALE = "Male"
  GENDER_FEMALE = "Female"
  VALIDATION_REGEX = "\d{10}"
  ADDITION_19S = 20
  ADDITION_21S = 40
  WEIGHTS = [2, 4, 8, 5, 10, 9, 7, 3, 6]
  REGIONS = [
      43, 93, 139, 169, 183,
      217, 233, 281, 301, 319,
      341, 377, 395, 435, 501,
      527, 555, 575, 601, 623,
      721, 751, 789, 821, 843,
      871, 903, 925, 999]
      
  REGION_NAMES = [
      "Blagoevgrad", "Burgas", "Varna",
      "Veliko Tarnovo", "Vidin", "Vratsa",
      "Gabrovo", "Kardzhali", "Kyustendil",
      "Lovech", "Montana", "Pazardzhik",
      "Pernik", "Pleven", "Plovdiv",
      "Razgrad", "Ruse", "Silistra",
      "Sliven", "Smolyan", "Sofia-grad",
      "Sofia-oblast", "Stara Zagora",
      "Dobrich", "Targovishte", "Haskovo",
      "Shumen", "Yambol", "Other/unknown"]

  def __init__(self, egn):
      self.egn = egn
      self.validate()
      self.calc_data()

  def calc_data(self):
      self.month = self.calc_month()
      self.year = self.calc_year()
      self.day = self.calc_day()
      self.gender = self.calc_gender()
      self.region = self.calc_region()

  def calc_month(self):
      self.month_raw = int(self.egn[2:4])

      if self.month_raw > Egn.ADDITION_21S:
          return (self.month_raw -
              Egn.ADDITION_21S)

      elif self.month_raw > Egn.ADDITION_19S:
          return (self.month_raw -
              Egn.ADDITION_19S)

      return self.month_raw

  def calc_year(self):
      if (self.month_raw > Egn.ADDITION_19S and
          self.month_raw < Egn.ADDITION_21S):
            year_prefix = "18"
      elif self.month_raw > Egn.ADDITION_21S:
          year_prefix = "20"
      else:
          year_prefix = "19"

      return year_prefix + str(self.egn[:2])
    
  def calc_day(self):
      return self.egn[4:6]

  def calc_gender(self):
      gender_number = int(self.egn[8])

      if gender_number % 2:
          return Egn.GENDER_FEMALE

      return Egn.GENDER_MALE
      
  def calc_region(self):
      region_id = int(self.egn[6:9])
      
      for i, region in enumerate(
              Egn.REGIONS):
          if region_id <= region:
              return Egn.REGION_NAMES[i]
    
  def validate(self):
      valid = True
      regex = re.compile(Egn.VALIDATION_REGEX)
      valid = re.match(regex, self.egn)
      expected_sum = int(self.egn[9])
      
      if expected_sum != self.calc_checksum():
          valid = False
      
      if not valid:
          raise RuntimeError("Invalid EGN")
          
  def calc_checksum(self):
      check_digit = 0

      for i, weight in enumerate(Egn.WEIGHTS):
          digit = int(self.egn[i])
          check_digit += digit * weight
          
      check_digit = check_digit % 11
      
      if check_digit >= 10:
          return 0

      return check_digit

  def __str__(self):
      return ("Year: " + self.year +
              "\nMonth: " + str(self.month) +
              "\nDay: " + self.day +
              "\nGender: " + self.gender +
              "\nRegion: " + self.region)
