class CompanyQuerySetMixin:
    """
    Garante que o usuário só veja dados da própria empresa
    """

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(company=user.company)
    
class CompanyCreateMixin:
    """
    Força o vínculo com a empresa do usuário logado
    """

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)
