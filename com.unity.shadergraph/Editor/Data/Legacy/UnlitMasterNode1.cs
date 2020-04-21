﻿using System;
using System.Collections.Generic;
using UnityEditor.Graphing;

namespace UnityEditor.ShaderGraph.Legacy
{
    class UnlitMasterNode1 : MasterNode1
    {
        public enum SurfaceType
        {
            Opaque,
            Transparent
        }

        public enum AlphaMode
        {
            Alpha,
            Premultiply,
            Additive,
            Multiply
        }

        public SurfaceType m_SurfaceType;
        public AlphaMode m_AlphaMode;
        public bool m_TwoSided;
        public bool m_AddPrecomputedVelocity;
        public bool m_DOTSInstancing;
        public string m_ShaderGUIOverride;
        public bool m_OverrideEnabled;
    }
}
