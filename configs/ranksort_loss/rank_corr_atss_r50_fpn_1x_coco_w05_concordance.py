_base_ = './ranksort_atss_r50_fpn_1x_coco.py'

model = dict(
    bbox_head=dict(
        type='RankCorrATSSHead',
        corr_w=0.5,
        corr_type='concordance'
        ))
