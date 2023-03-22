import jnius_config
import pandas
jnius_config.add_classpath('jedai-core-3.2.1-jar-with-dependencies.jar')
from jnius import autoclass

pathList = ['D:\\MyUniversity\\HK222\\DataMining\\Assignment\\datasets\\amazonProfiles',
            'D:\\MyUniversity\\HK222\\DataMining\\Assignment\\datasets\\gpProfiles']

dataframes = ['amazonProfiles', 'gpProfiles']

entityProfileList = []
idPairs = []


def readProfiles():
    for path, fileName in zip(pathList, dataframes):
        EntitySerializationReader = autoclass("org.scify.jedai.datareader.entityreader.EntitySerializationReader")
        data=EntitySerializationReader(path)
        entityProfiles=data.getEntityProfiles()
        entityProfileList.append(entityProfiles)
        profilesIterator = entityProfiles.iterator()
        profiles=[]
        while profilesIterator.hasNext():
                profile = profilesIterator.next()
                pf = {"id": len(profiles)}
                attributesIterator = profile.getAttributes().iterator()
                while attributesIterator.hasNext():
                    attribute = attributesIterator.next()
                    pf[attribute.getName()] = attribute.getValue()
                profiles.append(pf)

        df = pandas.DataFrame(profiles)

        df.to_csv(f'{fileName}.csv', index= False)

def readGroundTruth():
    groundTruthPath = 'D:\\MyUniversity\\HK222\\DataMining\\Assignment\\datasets\\amazonGpIdDuplicates'

    GroundTruthReader = autoclass("org.scify.jedai.datareader.groundtruthreader.GtSerializationReader")

    groundTruth = GroundTruthReader(groundTruthPath)

    groundTruthPairs = groundTruth.getDuplicatePairs(entityProfileList[0], entityProfileList[1])

    pairsIterator = groundTruthPairs.iterator()

    while pairsIterator.hasNext():
        pair = pairsIterator.next()
        entityId1 = pair.getEntityId1()
        entityId2 = pair.getEntityId2()
        idPairs.append((entityId1, entityId2))

    print(idPairs[:5])

readProfiles()

readGroundTruth()