from Bio import Entrez

# The PubMed API is called the Entrez Database
# db=pubmed, to narrow the search down to the pubmed DB only
# retmode=json, to have a JSON string in response and not an XML
# retmax=20, to obtain 20 results
# sort=relevance, the results are sorted by relevance and not by added date which is the default ranking option on pubmed
# term=[your query], the URL-encoded query

# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=20&sort=relevance&term=fever
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=30414522,30594188
def search(query):
    Entrez.email = 'ice-melt@outlook.com'
    handle = Entrez.esearch(db='pubmed',
                            sort='relevance',
                            retmax='20',
                            retmode='xml',
                            term=query)
    results = Entrez.read(handle)
    return results


def fetch_details(_id_list):
    ids = ','.join(_id_list)
    Entrez.email = 'ice-melt@outlook.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results


if __name__ == '__main__':
    search_results = search('fever')
    id_list = search_results['IdList']
    papers = fetch_details(id_list)
    # for i, paper in enumerate(papers):
    for i, paper in enumerate(papers['PubmedArticle']):
        print("%d) %s" % (i + 1, paper['MedlineCitation']['Article']['ArticleTitle']))
    # Pretty print the first paper in full to observe its structure
    # import json
    # print(json.dumps(papers[0], indent=2, separators=(',', ':')))

    """
    # results
    # 1) Noninfectious Fever in Aneurysmal Subarachnoid Hemorrhage: Association with Cerebral Vasospasm and Clinical Outcome.
    # 2) Coronary artery status of patients with transient fever 24-36 h after first IVIG infusion did not differ from that seen in responsive patients.
    # 3) National Trends in Hospitalization for Fever and Neutropenia in Children with Cancer, 2007-2014.
    # 4) Fever-related arrhythmic events in the multicenter Survey on Arrhythmic Events in Brugada Syndrome.
    # 5) Duration of fever and other symptoms after the inhalation of laninamivir octanoate hydrate in the 2016/17 Japanese influenza season; comparison with the 2011/12 to 2015/16 seasons.
    # 6) Post-immunisation fever and the antibody response to measles-containing vaccines.
    # 7) Neural Mechanisms of Inflammation-Induced Fever.
    # 8) Fever and systemic inflammatory response syndrome after retrograde intrarenal surgery: Risk factors and predictive model.
    # 9) Fever Responses Are Enhanced with Advancing Age during Respiratory Syncytial Virus Infection among Children under 24 Months Old.
    # 10) Early postoperative fever workup in children: utilization and utility.
    # 11) Behavioral fever decreases metabolic response to lipopolysaccharide in yellow Cururu toads (Rhinella icterica).
    # 12) Predictive Factors of Fever After Aneurysmal Subarachnoid Hemorrhage and Its Impact on Delayed Cerebral Ischemia and Clinical Outcomes.
    # 13) Risk Factors for Chest Pain and Fever in Patients Undergoing Pleurodesis with OK-432.
    # 14) Intrapartum fever and the risk for perinatal complications - the effect of fever duration and positive cultures.
    # 15) Clinical evaluation of postoperative fever in patients that had oral and maxillofacial surgery in university of Nigeria Teaching Hospital, Ituku-Ozalla, Enugu, Nigeria.
    # 16) Fever and prodromal infections in anti-glomerular basement membrane disease.
    # 17) Treatable causes of fever among children under five years in a seasonal malaria transmission area in Burkina Faso.
    # 18) Tri-phasic fever in dengue fever.
    # 19) Rotavirus infection as a frequent cause of neonatal fever.
    # 20) Non-severe form of severe fever with thrombocytopenia syndrome (SFTS).
    """
