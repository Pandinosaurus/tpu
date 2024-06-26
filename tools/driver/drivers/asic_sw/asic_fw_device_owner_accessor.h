/* SPDX-License-Identifier: GPL-2.0 */
/*
 * Copyright (C) 2021 Google LLC.
 */
#ifndef _DRIVERS_ASIC_SW_ASIC_FW_DEVICE_OWNER_ACCESSOR_H_
#define _DRIVERS_ASIC_SW_ASIC_FW_DEVICE_OWNER_ACCESSOR_H_ 
#include "drivers/gasket/gasket_types.h"
static inline uint64_t asic_fw_device_owner_value(const uint64_t reg_value)
{
 return (uint64_t)((((reg_value >> 0) & 0xffffffffffffffffULL) << 0));
}
static inline int set_asic_fw_device_owner_value(uint64_t *reg_value,
       uint64_t value)
{
 if ((uint64_t)value < 0x0ULL || (uint64_t)value > 0xffffffffffffffffULL)
  return 1;
 (*reg_value) = ((*reg_value) & ~((0xffffffffffffffffULL) << 0)) |
         (((value >> 0) & (0xffffffffffffffffULL)) << 0);
 return 0;
}
#endif
