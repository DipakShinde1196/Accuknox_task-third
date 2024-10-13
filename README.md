Question 3: By default, do Django signals run in the same database transaction as the caller?

Yes, by default, Django signals run in the same database transaction as the caller. This means that if a signal is sent during a transaction, and the transaction is rolled back, any database operations performed by the signal receivers will also be rolled back.
