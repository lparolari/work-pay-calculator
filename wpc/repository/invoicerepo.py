from wpc.repository.crudrepo import CrudRepo
from wpc.model.invoice import Invoice
from wpc.model.invoice_with_hours import InvoiceWithHours
from wpc.model.work import Work
from sqlalchemy import func, and_


class InvoiceRepo(CrudRepo):

    def __init__(self, clazz=Invoice):
        super().__init__(clazz)

    def _q(self, clazz=None):
        q = super(CrudRepo, self)._q(clazz)

        if clazz is None:
            q.filter(Invoice.customer_id == super()._configurator.customer)
            q.order_by(Invoice.emitted_at.desc(), Invoice.from_dt.desc())

        return q

    #def _q_def(self):
    #    return self._q()\
    #        .filter(Invoice.customer_id == super()._configurator.customer)\
    #        .order_by(Invoice.emitted_at.desc(), Invoice.from_dt.desc())

    def getAll(self, *criterion):
        return self._q().all()

    def getAllWithHours(self):
        return self._q(InvoiceWithHours) \
            .filter(InvoiceWithHours.customer_id == super()._configurator.customer) \
            .order_by(InvoiceWithHours.emitted_at.desc(), InvoiceWithHours.from_dt.desc())\
            .all()

    def getEmittedBetweenWithHours(self, begin, end):
        return self._q(InvoiceWithHours) \
            .filter(InvoiceWithHours.customer_id == super()._configurator.customer) \
            .filter(InvoiceWithHours.emitted_at >= begin) \
            .filter(InvoiceWithHours.emitted_at <= end) \
            .order_by(InvoiceWithHours.emitted_at.desc(), InvoiceWithHours.from_dt.desc())\
            .all()
