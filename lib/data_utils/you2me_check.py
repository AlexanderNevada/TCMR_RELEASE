import os.path as osp
import glob
import tqdm
import json

# cmu check
cmu_path = '/media/qimaqi/Alexander/you2me/cmu'
# /media/qimaqi/Alexander/you2me/cmu/1-catch1/features/openpose/output_json
json_list = glob.glob(osp.join(cmu_path,'*','*','*','*','*.json'))
# print(len(json_list)) # 43249
# empty_file = 0
# for file in tqdm.tqdm(json_list):
#     json_data = json.load(open(file, 'r'))
#     people = json_data['people']
#     if len(people) == 0:
#         empty_file+=1

# print('empty_file number', empty_file)

# 'kinect check
kinect_path = '/media/qimaqi/Alexander/you2me/kinect'
json_list = glob.glob(osp.join(kinect_path,'*','*','*','*','*.json'))
print(len(json_list)) # 43249
empty_file = 0
for file in tqdm.tqdm(json_list):
    json_data = json.load(open(file, 'r'))
    people = json_data['people']
    if len(people) == 0:
        empty_file+=1

print('len of kinect empty',empty_file)

# def read_openpose(json_file): # gt_part
#         # get only the arms/legs joints
#     op_to_12 = [11, 10, 9, 12, 13, 14, 4, 3, 2, 5, 6, 7]
#     # read the openpose detection
#     json_data = json.load(open(json_file, 'r'))
#     people = json_data['people']
#     if len(people) == 0:
#         # no openpose detection
#         keyp25 = np.zeros([25,3])
#     else:
#         # size of person in pixels
#         # TODO scale of person
#         #scale = max(max(gt_part[:,0])-min(gt_part[:,0]),max(gt_part[:,1])-min(gt_part[:,1]))
#         # go through all people and find a match
#         dist_conf = np.inf*np.ones(len(people))
#         for i, person in enumerate(people):
#             # openpose keypoints
#             op_keyp25 = np.reshape(person['pose_keypoints_2d'], [25,3])
#             op_keyp12 = op_keyp25[op_to_12, :2]
#             op_conf12 = op_keyp25[op_to_12, 2:3] 
#             # all the relevant joints should be detected
#             if min(op_conf12) > 0:
#                 # weighted distance of keypoints
#                 # TODO try just get the closest one
#                 # print('op_conf12',op_conf12,np.shape(op_conf12))
#                 # print('op_keyp12',op_keyp12,np.shape(op_keyp12))
#                 dist_conf[i] = np.mean(op_conf12) # select most high conf one
#                 # np.mean(np.sum(op_conf12*op_keyp12), axis=1) # *(op_keyp12 - gt_part[:12, :2]
#         # closest match
#         # There maybe many matches and here we only wnat the cloest
#         p_sel = np.argmin(dist_conf)
#         # the exact threshold is not super important but these are the values we used
#         thresh = 0
#         # dataset-specific thresholding based on pixel size of person
#         #if min(dist_conf)/scale > 0.1 and min(dist_conf) < thresh:
#         #    keyp25 = np.zeros([25,3])
#         #else:
#         keyp25 = np.reshape(people[p_sel]['pose_keypoints_2d'], [25,3])
#     return keyp25