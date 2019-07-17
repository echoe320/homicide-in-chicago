import csv
import json

print('Opening the CSV...')
f = open('/mnt/c/Users/cpd3149/web/homicide-in-chicago/data/homicide-data.csv')

print('Changing fieldnames...')
reader = csv.DictReader(f, fieldnames = ("IndexId","CaseDescription", "CaseDescriptionCaseNumber", "CircumstancesAddress", "CircumstancesAlcoholRelated", "CircumstancesCharacteristics", "CircumstancesCircumstancesDescription", "CircumstancesCircumstancesOfCivilUnrest", "CircumstancesDateOfDeath", "CircumstancesDateOfOffense", "CircumstancesExcessiveViolence", "CircumstancesGovernment/SpecialForcesPresent", "CircumstancesLocationDescription", "CircumstancesMethodOfKilling", "CircumstancesMotive", "CircumstancesMurder/Suicide", "CircumstancesOtherRelatedOrganizedCrimeIndicators", "CircumstancesOtherRelatedProhibitionIndicators", "CircumstancesPresenceOfFederalAgents", "CircumstancesProhibition-RelatedLocation", "CircumstancesRelatedToCivilUnrest", "CircumstancesRelatedToOrganizedCrime", "CircumstancesRelatedToProhibition", "CircumstancesTimeBetweenOffenseAndDeath", "CircumstancesTimeOfDay(Approx)", "CircumstancesTimeOfDay(Exact)", "CircumstancesTotalNumberOfDefendants", "CircumstancesTotalNumberOfVictims", "CircumstancesTypeOfAccident", "CircumstancesTypeOfBusiness", "CircumstancesTypeOfCivilUnrest", "CircumstancesTypeOfDeath", "CircumstancesTypeOfHomicide", "CircumstancesTypeOfLocation", "CircumstancesTypeOfManslaughter", "CircumstancesTypeOfMedicalFacility", "CircumstancesTypeOfPublicPlace", "CircumstancesTypeOfResidence", "CircumstancesTypeOfVehicle", "CircumstancesVictimInitiatedEventsLeadingToHomicide", "CircumstancesWeapon", "DefendantAge", "DefendantBusinessOwner", "DefendantDefendant/VictimRelationship", "DefendantEmployed", "DefendantEmploymentType", "DefendantEthnicity", "DefendantGender", "DefendantKillingWhileProtectingPerson", "DefendantKillingWhileProtectingProperty", "DefendantKillingWhileProvidingMedicalServicesAsA", "DefendantKnownToChicagoPoliceAs", "DefendantName", "DefendantOccupationalSkill", "DefendantPriorNon-FamilyRelationship", "DefendantRace", "DefendantRelatedByBloodOrMarriage", "LegalAllegationsOfPoliceCorruption", "LegalBailset", "LegalChargesAgainstDefendant", "LegalCircumstancesSuggestingJudicialCorruption", "LegalDateClemencyGranted", "LegalDateOfCoronerSDecision", "LegalDateOfExecution", "LegalDateOfGrandJuryDecision", "LegalDateOfSentence", "LegalDateTrialStarted", "LegalDefendantExecuted", "LegalFelonyMurderClassification", "LegalGovernorCommutedDeathToLifeOrChangedSentence", "LegalHigherCourtAction", "LegalJudgeAssociatedWithBail", "LegalJudgeOfSecondTrial", "LegalJudgementReversedOnAppeal", "LegalJuryVerdict", "LegalLengthOfSentence", "LegalLocationOfCourt", "LegalNumberOfTimesCaseStrickenOff", "LegalOutcomeOfCoronerSJudgement", "LegalOutcomeOfGrandJuryDecision", "LegalOutcomeOfSecondTrial", "LegalOutcomeOfTrial", "LegalPostTrialInformation", "LegalRetrial", "LegalSentenceCompleted", "LegalSentencedTo", "LegalTrialJudge", "LegalTypeOfExecution", "LegalTypeOfLegalDecisionRecorded", "PoliceAllegationsOfPoliceCorruption", "PoliceArrestMadeAtCrimeScene", "PoliceDateDefendantArrested", "PoliceDefendantEmployedInLawEnforcement", "PoliceDefendantIdDAtScene", "PoliceLocationOfArrest", "PolicePrecinct", "PoliceTimeBetweenCrimeAndArrest", "PoliceTotalNumberOfDefendantsArrested", "PoliceVictimEmployedInLawEnforcement", "VictimAge", "VictimBusinessOwner", "VictimEmployed", "VictimEmploymentType", "VictimEthnicity", "VictimGender", "VictimKilledWhileProtectingPerson", "VictimKilledWhileProtectingProperty", "VictimKnownToChicagoPoliceAs", "VictimName", "VictimNameOfHospitalWhereVictimWasTaken", "VictimOccupationalSkill", "VictimPriorNon-FamilyRelationship", "VictimRace", "VictimRelatedByBloodOrMarriage", "VictimVictim/DefendantRelationship"))
out = json.dumps([row for row in reader])
print('JSON is parsed!')
f = open('/mnt/c/Users/cpd3149/web/homicide-in-chicago/data/homicide-data.json', 'w')
f.write(out)
print('JSON is saved!')