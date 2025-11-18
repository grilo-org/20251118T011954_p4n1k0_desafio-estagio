# Importações (Simulação: em um ambiente real, seria necessário instalar transformers)
# from transformers import pipeline
# generator = pipeline("text-generation", model="distilgpt2")

# Estrutura de dados para leads e templates de personalização
new_leads = [
    {'setor': 'Tecnologia', 'nome': 'Union Tech Solutions'},
    {'setor': 'Saúde', 'nome': 'Clínica Bem-Estar'},
    {'setor': 'Indústria', 'nome': 'Metalúrgica Alfa'}
]

# Dicionário de Personalização (Prompt Engineering Simples)
# O modelo de linguagem usará o "tone" e "keywords" para personalizar a saída.
personalization_profiles = {
    'Tecnologia': {
        'tom': "direto, focado em escalabilidade e inovação",
        'assunto': "Alavanque sua infraestrutura com o Union IT Pro.",
        'keywords': "escalabilidade, automação de processos, ROI, integração API"
    },
    'Saúde': {
        'tom': "empático, focado em segurança de dados e eficiência",
        'assunto': "Garanta a LGPD e otimize a gestão de pacientes.",
        'keywords': "segurança de dados, LGPD, prontuário eletrônico, conformidade"
    },
    'Indústria': {
        'tom': "prático, focado em eficiência operacional e redução de custos",
        'assunto': "Otimize sua linha de produção com o Union IT.",
        'keywords': "eficiência operacional, IoT industrial, manutenção preditiva, redução de *downtime*"
    }
}

def generate_marketing_email(lead_data):
    """
    Gera um rascunho de e-mail marketing adaptado ao setor do lead.
    """
    setor = lead_data['setor']
    nome_empresa = lead_data['nome']
    
    # Define o perfil de personalização ou usa um perfil padrão
    profile = personalization_profiles.get(setor, {
        'tom': "neutro, focado em benefícios gerais",
        'assunto': f"Descubra como Union IT pode transformar {setor}.",
        'keywords': "transformação digital, produtividade, suporte dedicado"
    })
    
    # Prompt base (o 'input' real para o modelo de linguagem)
    prompt = f"""
    Crie um rascunho de e-mail marketing para a empresa {nome_empresa}, do setor de {setor}. 
    O tom deve ser {profile['tom']}. O assunto é: "{profile['assunto']}". 
    O e-mail deve incluir uma breve introdução, destacar um benefício chave usando as keywords: {profile['keywords']} e terminar com um Call to Action (CTA).
    """
    
    # Simulação da Geração (No ambiente real, generator(prompt, max_length=...)[0]['generated_text'] seria usado)
    if setor == 'Tecnologia':
        email_body = f"Olá {nome_empresa},\n\nNós da Union IT entendemos o seu desafio de **escalabilidade**. Nosso serviço foi desenhado para maximizar o seu **ROI** através da **automação de processos** e **integração API** simplificada. Queremos agendar uma demonstração rápida para mostrar o potencial de crescimento."
    elif setor == 'Saúde':
        email_body = f"Prezado(a) responsável pela {nome_empresa},\n\nA **segurança de dados** e a **conformidade LGPD** são cruciais no setor de Saúde. Nossa plataforma garante que sua gestão de **prontuário eletrônico** seja eficiente e segura. Responda a este e-mail para agendar uma consultoria gratuita sobre como podemos proteger seus dados."
    else:
        email_body = f"Caro(a) gestor(a) da {nome_empresa},\n\nFocamos em resultados reais. Descubra como nossa solução está transformando a **eficiência operacional** de empresas no setor {setor}. Queremos mostrar como reduzir o ***downtime*** e economizar."
    
    return f"Assunto: {profile['assunto']}\n\nCorpo:\n{email_body}\n\n[CTA: Saiba Mais / Agende uma demonstração]"

# Execução do Protótipo
for lead in new_leads:
    print(f"\n--- E-mail para o Setor: {lead['setor']} ---")
    print(generate_marketing_email(lead))
