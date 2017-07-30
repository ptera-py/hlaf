#Объект класса содержит конкретного Human и все значения одной метрики.
class OneMetric:
    #Конструктор принимает Human и object_set одной связанной метрики
    def __init__(self, human, l_ObjectSet, N=10):
        self.human = human
        self.metric_all = l_ObjectSet.order_by('-m_date')
        self.metric_N = l_ObjectSet.order_by('-m_date')[:N]
        self.model_fields = l_ObjectSet.model._meta.fields
        self.metric_all_l = [] #все значения метрики в виде списка списков
        for metric in self.metric_all:
            t_list=[] #промежуточный список
            for field in self.model_fields:
                t_list.append(getattr(metric,field.name))
            self.metric_all_l.append(t_list)
        self.metric_N_l = self.metric_all_l[:N]
