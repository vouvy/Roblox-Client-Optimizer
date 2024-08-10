<h1 align="center">
<table>
<tr>
<td>
However, this may not be suitable for everyone It was created for my personal use only Please use it with caution
</td>
</tr>
</table>

---

<h1 align="center">
  <br>
  Roblox Client Optimizer (FFlags)
  <br>
</h1>

> [!CAUTION]
> "**FFlags**" can pose security risks as they allow for specific system-level configurations and optimizations, which might inadvertently expose sensitive data or system vulnerabilities if not managed correctly. Improper use or configuration of FFlags could lead to unintended security issues or performance degradation.

---

<h1 align="center">
  <br>
  Bloxstrap Preset (FFlags)
  <br>
</h1>

```json
{
  "FLogNetwork": "7",
  "FFlagDisableNewIGMinDUA": "True",
  "FFlagEnableInGameMenuControls": "True",
  "FFlagEnableInGameMenuModernization": "True",
  "FFlagEnableInGameMenuChrome": "True",
  "FFlagEnableMenuControlsABTest": "False",
  "FFlagEnableV3MenuABTest3": "False",
  "FFlagEnableInGameMenuChromeABTest3": "False",
  "FFlagFixGraphicsQuality": "True",
  "DFFlagDisableDPIScale": "True",
  "FIntFRMMinGrassDistance": "0",
  "DFIntCSGLevelOfDetailSwitchingDistanceL12": "0",
  "FFlagDebugGraphicsPreferD3D11FL10": "True",
  "DFIntCSGLevelOfDetailSwitchingDistance": "0",
  "FIntFRMMaxGrassDistance": "0",
  "DFIntCSGLevelOfDetailSwitchingDistanceL34": "0",
  "FFlagRenderFixFog": "True",
  "FFlagDebugSkyGray": "True",
  "FFlagTaskSchedulerLimitTargetFpsTo2402": "False",
  "DFFlagDebugRenderForceTechnologyVoxel": "True",
  "DFIntCSGLevelOfDetailSwitchingDistanceL23": "0",
  "FFlagDisablePostFx": "True",
  "FFlagDebugGraphicsPreferOpenGL": "True",
  "DFFlagDebugSkipMeshVoxelizer": "True",
  "FIntRenderGrassDetailStrands": "0",
  "FIntFullscreenTitleBarTriggerDelayMillis": "3600000",
  "FIntDebugForceMSAASamples": "1",
  "FFlagGameBasicSettingsFramerateCap5": "False",
  "DFFlagDebugPauseVoxelizer": "True",
  "FIntTerrainArraySliceSize": "0",
  "FIntRenderShadowIntensity": "0",
  "DFIntTaskSchedulerTargetFps": "5588562",
  "DFIntDebugRestrictGCDistance": "1",
  "DFFlagTextureQualityOverrideEnabled": "True",
  "DFIntTextureQualityOverride": "0",
  "DFIntConnectionMTUSize": "1464",
  "DFIntRakNetMtuValue1InBytes": "1464",
  "DFIntRakNetMtuValue2InBytes": "1464",
  "DFIntRakNetMtuValue3InBytes": "1464"
}
```

> [!TIP]
> If you encounter a low-quality texture issue, you can adjust the DFIntTextureQualityOverride value from 0 to 5 to resolve the problem


---

<h1 align="center">
  <br>
  MTU Configuration
  <br>
</h1>

**If you need to find the optimal MTU value for your network, you can utilize this code to determine the most suitable setting**

```python
import subprocess  # Import the subprocess module to run system commands.

def ping_test(host, packet_size):
    # Define a function to test if a specific packet size can be sent to a host without fragmentation.
    try:
        result = subprocess.run(
            ["ping", host, "-f", "-l", str(packet_size)],  # Run the ping command with flags: -f (do not fragment) and -l (set packet size).
            capture_output=True,  # Capture the output of the command.
            text=True,  # Ensure the output is returned as a string.
            timeout=5  # Set a timeout of 5 seconds for the command.
        )
        output = result.stdout  # Get the standard output from the result.
        if "Packet needs to be fragmented but DF set" in output:
            # Check if the output contains the message indicating that the packet needs to be fragmented.
            return False  # Return False if fragmentation is needed.
        return True  # Return True if the packet size did not require fragmentation.
    except subprocess.TimeoutExpired:
        # Handle the case where the subprocess command times out.
        return False  # Return False if the command times out.

def find_optimal_mtu(host):
    # Define a function to find the optimal MTU size for a given host.
    max_mtu = 1472  # Set the maximum MTU size to test.
    min_mtu = 1000  # Set the minimum MTU size to test.
    optimal_mtu = min_mtu  # Initialize the optimal MTU with the minimum value.

    for mtu in range(max_mtu, min_mtu, -1):
        # Iterate over possible MTU sizes from max_mtu down to min_mtu.
        if ping_test(host, mtu):
            # Test if the current MTU size is valid using the ping_test function.
            optimal_mtu = mtu  # Update the optimal MTU if the current size is valid.
            break  # Exit the loop as soon as a valid MTU size is found.

    return optimal_mtu  # Return the optimal MTU size.

if __name__ == "__main__":
    host = "roblox.com"  # Define the host to test the MTU size with.
    optimal_mtu = find_optimal_mtu(host)  # Find the optimal MTU size for the host.
    print(f"The optimal MTU size is: {optimal_mtu} bytes")  # Print the optimal MTU size.
```
> **This will affect your in-game ping, so it's recommended to set your MTU to the optimal value**

**Windows + R and type**
```
netsh interface ipv4 show subinterfaces
```
