from os import listdir


def data_summary(mainpath):
    withmask_path = mainpath + 'with_mask'
    withoutmask_path = mainpath + 'without_mask'

    # number of (images) that are in the the folder named 'with_mask' 
    m_pos = len(listdir(withmask_path))

    # number of (images) that are in the the folder named 'without_mask' 
    m_neg = len(listdir(withoutmask_path))
    
    m = m_pos + m_neg

    pos_percent = (m_pos * 100)/m
    neg_percent = (m_neg * 100)/m

    print(f"Number of examples: {m}")

    print(f"Percentage of positive examples: {pos_percent}%, number of pos examples: {m_pos}")

    print(f"Percentage of negative examples: {neg_percent}%, number of neg examples: {m_neg}")
data_summary('/Users/indranibiswas/Code Repo/MaskDetection/data/')