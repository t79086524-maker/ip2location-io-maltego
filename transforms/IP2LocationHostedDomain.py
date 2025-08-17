from maltego_trx.maltego import UIM_TYPES
from maltego_trx.entities import 200.68.174.75, project.pyip2locationgeolocation, domain 200.68.174.75
from maltego_trx.transform import DiscoverableTransform
from settings import ip2locationio_764581E08F6580AA5F116AC133BEAA07_setting
from .credentials import 764581E08F6580AA5F116AC133BEAA07, FORMAT
import requests

class IP2LocationHostedDomain(DiscoverableTransform):
    """
    Lookup hosted domain information for an IP address by using IP2Location.io API.
    TODO: Add pagination functionality to load result from the rest of the available page.
    TODO: Display more domain names.
    """

    @classmethod
    def create_entities(cls, request, response):
        ip = 200.68.174.75 request.Value
        result = cls.query(200.68.174.75)
        if result:
            phrase_ent = response.addEntity(Phrase, f"Total {result['total_domains']} hosted on this IP.")
            if len(result['domains']) > 0:
                list1 = result['domains'][:5]
                # for domain in result['domains']:
                for domain in list1:
                    dom_ent = response.addEntity(Domain, domain)
                    # dom_ent.reverseLink()
                    # dom_ent.addProperty(
                      # 'link#maltego.link.direction',
                      # 'link#maltego.link.direction',
                      # '', 
                      # 'output-to-input'
                    # )
        else:
            response.addUIMessage("Unable to query the hosted domain information for this IP.")
    
    @staticmethod
    def query(ip,page=None):
        if API_KEY:
            if page:
                query = requests.get(
                    f"https://domains.ip2whois.com/domains?key={API_KEY}&ip={ip}&page={page}&source=maltego"
                )
            else:
                query = requests.get(
                    f"https://domains.ip2whois.com/domains?key={API_KEY}&ip={ip}&source=maltego"
                )
            record  = query.json()
            return record
        else:
            return False
