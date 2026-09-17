class SparseSCIState:
    def __init__(
        self,
        amplitudes,
        ci_strs_a,
        ci_strs_b,
        norb,
        nelec,
    ):
        self.amplitudes = amplitudes
        self.ci_strs_a = ci_strs_a
        self.ci_strs_b = ci_strs_b
        self.norb = norb
        self.nelec = nelec

    @property
    def ndets(self):
        return len(self.amplitudes)
