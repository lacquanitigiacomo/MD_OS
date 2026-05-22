"""
MD_OS v11 "Chimera" — Core Engine
Sistema operativo minimale per automazione intelligente on-device.
Zero API esterne. Zero costi. 100% locale.
"""
__version__ = "11.0.0"
__codename__ = "Chimera"

from .nucleo import Nucleo
from .memoria import MemoriaGerarchica
from .ragionamento import RagionamentoTemplate
from .skill_registry import SkillRegistry

__all__ = ["Nucleo", "MemoriaGerarchica", "RagionamentoTemplate", "SkillRegistry"]
