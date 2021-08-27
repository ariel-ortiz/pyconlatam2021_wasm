(module
  (func $calcular_pi (export "calcular_pi")
    (param $p0 i32)
    (result f64)
    (local $l0 f64)
    (local $l1 f64)
    (local $l2 f64)
    (local $l3 f64)
    f64.const 1
    local.get $p0
    f64.convert_i32_s
    f64.div
    local.set $l0
    f64.const 0
    local.set $l1
    block $B0
      local.get $p0
      i32.const 1
      i32.lt_s
      br_if $B0
      f64.const 0
      local.set $l2
      loop $L1
        local.get $l1
        f64.const 4
        local.get $l0
        local.get $l2
        f64.const 0.5
        f64.add
        f64.mul
        local.tee $l3
        local.get $l3
        f64.mul
        f64.const 1
        f64.add
        f64.div
        f64.add
        local.set $l1
        local.get $l2
        f64.const 1
        f64.add
        local.set $l2
        local.get $p0
        i32.const -1
        i32.add
        local.tee $p0
        br_if $L1
      end
    end
    local.get $l0
    local.get $l1
    f64.mul
  )
)
