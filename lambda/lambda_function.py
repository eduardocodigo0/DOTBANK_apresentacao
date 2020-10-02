# -*- coding: utf-8 -*-

import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import StandardCard
from ask_sdk_model.ui.image import Image

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

imagem_padrao = Image("https://i.imgur.com/VxXfaz3.jpg", "https://i.imgur.com/VxXfaz3.jpg")

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        speak_output = "Bem vindo ao Dóti Benk. Como posso te ajudar?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


#=========== Minhas Classes ========================


class saldoBancarioIntentHandler (AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("saldoBancarioIntent")(handler_input)

    def handle(self, handler_input):
        
        speak_output = "Olá, Marcelo, seu saldo é de 21.370 reais."
        card_text = "Saldo: R$21.370,00"
            
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_card(StandardCard("Saldo", card_text, imagem_padrao))
                .ask("Posso ajudar em mais alguma coisa?")
                .response
        )

class pagementoPeriodoIntent (AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pagementoPeriodoIntent")(handler_input)

    def handle(self, handler_input):
        
        speak_output = "Você tem uma conta de energia elétrica no valor de 210 reais e 35 centavos. e o pagamento do fornecedor de móveis no valor de 654 reais."
        card_text = "\nEnergia Elétrica: R$210,35.\n\nFornecedor de móveis: R$654,00"
            
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_card(StandardCard("Pagamentos", card_text, imagem_padrao))
                .ask("Posso ajudar em mais alguma coisa?")
                .response
        )

class realizarPagamentoIntent (AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("realizarPagamentoIntent")(handler_input)

    def handle(self, handler_input):
        
        speak_output = "Conta de energia paga com sucesso."
        card_text = "\nConta: Energia Elétrica R$210,35 foi paga com sucesso!"
            
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_card(StandardCard("Pagamentos", card_text, imagem_padrao))
                .ask("Posso ajudar em mais alguma coisa?")
                .response
        )

class volumeVendasIntent (AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("volumeVendasIntent")(handler_input)

    def handle(self, handler_input):
        
        speak_output = "Você vendeu 280147 reais em setembro."
        card_text = "\nVendas em Setembro: R$280.147,00"
            
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_card(StandardCard("Volume de vendas", card_text, imagem_padrao))
                .ask("Posso ajudar em mais alguma coisa?")
                .response
        )

class melhorVendedorIntent (AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("melhorVendedorIntent")(handler_input)

    def handle(self, handler_input):
        
        speak_output = "Seu melhor vendedor é o Pedro Rósa da empresa Vamos Parcelar"
        card_text = "\nVendedor: Pedro Rosa\n\n Empresa: Vamos Parcelar"
            
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_card(StandardCard("Melhor Vendedor", card_text, imagem_padrao))
                .ask("Posso ajudar em mais alguma coisa?")
                .response
        )


class agradeceIntent (AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("agradeceIntent")(handler_input)

    def handle(self, handler_input):
        
        speak_output = "Obrigado pela oportunidade de participar da batalha das startápis."
        card_text = "Obrigado pela oportunidade de participar da batalha das startups."
            
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_card(StandardCard("Obrigado", card_text,imagem_padrao))
                .response
        )

class pitchIntent (AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("pitchIntent")(handler_input)

    def handle(self, handler_input):
        
        speak_output = "Claro. o Dóti Benk é um banco digital que ajuda empresários a ganharem performance nas rotinas diárias além de pagamentos e recebimentos. com o meu apoio é possível fazer muitas tarefas. podemos ainda utilizar rôbôs para operações, minimizando erros humanos e aumentando a performance da empresa, além das reduções de custo."
        card_text = "Claro, o Dotbank é um banco digital que ajuda empresários a ganharem performance nas rotinas diárias além de pagamentos e recebimentos, com o meu apoio é possível fazer muitas tarefas, podemos ainda utilizar robôs para operações minimizando erros humanos e aumentando a performance da empresa além das reduções de custo."
            
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .set_card(StandardCard("Obrigado", card_text,imagem_padrao))
                .ask("Posso ajudar em mais alguma coisa?")
                .response
        )


#=========== Classes Padrao ========================

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Você pode me perguntar qual é o seu saldo, o que você tem para pagar hoje, qual foi o seu volume de vendas ou até mesmo para pagar uma conta"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Tchau!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "você ativou " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Desculpe, eu não entendi o que você pediu."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
#========CRIADOS===========================

sb.add_request_handler(saldoBancarioIntentHandler())
sb.add_request_handler(pagementoPeriodoIntent())
sb.add_request_handler(realizarPagamentoIntent())
sb.add_request_handler(volumeVendasIntent())
sb.add_request_handler(melhorVendedorIntent())
sb.add_request_handler(agradeceIntent())
sb.add_request_handler(pitchIntent())

#=========================================
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()