_base_ = './ranksort_paa_r50_fpn_1x_coco.py'

model = dict(
    bbox_head=dict(
        type='RankBasedCorrPAAHead',
        corr_w=0.2,
        corr_type='concordance'
        ))
