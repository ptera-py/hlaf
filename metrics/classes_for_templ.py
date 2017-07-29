#Объект класса содержит конкретного Human и все значения одной метрики.
class OneMetric:
    #Конструктор принимает Human и object_set одной связанной метрики
    def __init__(self, human, l_ObjectSet):
        self.human = human
        self.metric_all = l_ObjectSet.order_by('-m_date')
        self.metric_10 = l_ObjectSet.order_by('-m_date')[:10]
        self.model_fields = l_ObjectSet.model._meta.fields
        self.metric_all_l = [] #все значения метрики в виде списка списков
        for metric in self.metric_all:
            t_list=[] #промежуточный список
            for field in self.model_fields:
                t_list.append(getattr(metric,field.name))
            self.metric_all_l.append(t_list)
        self.metric_10_l = self.metric_all_l[:10]